import os
import re
import json
from flask import Flask, render_template, request

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import LLMChain

from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ===================== API KEY =====================
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not set in environment variables")

os.environ["OPENAI_API_KEY"] = api_key

# ===================== FLASK APP =====================
app = Flask(__name__)

general_exclusion_list = [
    "HIV/AIDS",
    "Parkinson's disease",
    "Alzheimer's disease",
    "pregnancy",
    "substance abuse",
    "self-inflicted injuries",
    "sexually transmitted diseases(std)",
    "pre-existing conditions"
]

# ===================== LOAD DOCUMENTS =====================
def get_document_loader():
    loader = DirectoryLoader("documents", glob="**/*.pdf", loader_cls=PyPDFLoader)
    return loader.load()

def get_text_chunks(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_documents(docs)

def get_vector_db():
    docs = get_document_loader()
    chunks = get_text_chunks(docs)
    return FAISS.from_documents(chunks, OpenAIEmbeddings())

vector_db = get_vector_db()

# ===================== CONTEXT FUNCTIONS =====================
def get_claim_approval_context():
    docs = vector_db.similarity_search("claim approval documents required")
    return " ".join([d.page_content for d in docs])

def get_general_exclusion_context():
    docs = vector_db.similarity_search("general exclusions list")
    return " ".join([d.page_content for d in docs])

# ===================== PDF TEXT =====================
def get_file_content(file):
    text = ""
    if file.filename.endswith(".pdf"):
        pdf = PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# ===================== BILL INFO EXTRACTION =====================
def get_bill_info(data):
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    prompt = f"""
Extract only JSON:
{{"disease":"", "expense":""}}

Invoice:
{data}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except:
        return {"disease": "", "expense": "0"}

# ===================== EXCLUSION CHECK =====================
def check_exclusion(claim_reason, exclusions, threshold=0.4):
    vectorizer = CountVectorizer()
    patient_vec = vectorizer.fit_transform([claim_reason])

    for disease in exclusions:
        try:
            disease_vec = vectorizer.transform([disease])
            sim = cosine_similarity(patient_vec, disease_vec)[0][0]

            if sim > threshold:
                return True, disease
        except:
            continue

    return False, None

# ===================== PROMPT =====================
PROMPT = """
You are an insurance claim verification AI.

CLAIM RULES:
- Reject if exclusion found
- Reject if documents incomplete

CLAIM CONTEXT:
{claim_approval_context}

EXCLUSIONS:
{general_exclusion_context}

PATIENT INFO:
{patient_info}

MEDICAL BILL:
{medical_bill_info}

MAX AMOUNT:
{max_amount}

Generate a structured report and final decision.
"""

prompt_template = PromptTemplate(
    input_variables=[
        "claim_approval_context",
        "general_exclusion_context",
        "patient_info",
        "medical_bill_info",
        "max_amount"
    ],
    template=PROMPT
)

# ===================== ROUTES =====================
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def process_claim():

    name = request.form["name"]
    address = request.form["address"]
    claim_type = request.form["claim_type"]
    claim_reason = request.form["claim_reason"]
    date = request.form["date"]
    medical_facility = request.form["medical_facility"]
    total_claim_amount = request.form["total_claim_amount"]
    description = request.form["description"]
    medical_bill = request.files["medical_bill"]

    bill_text = get_file_content(medical_bill)
    bill_info = get_bill_info(bill_text)

    expense = bill_info.get("expense", "0")

    # ---------------- VALIDATION ----------------
    try:
        expense = int(expense)
        claim_amount = int(total_claim_amount)
    except:
        return render_template("result.html", output="Invalid amount format")

    if expense < claim_amount:
        return render_template("result.html", output="Rejected: Claim amount exceeds bill")

    # ---------------- EXCLUSION CHECK ----------------
    flagged, disease = check_exclusion(claim_reason, general_exclusion_list)

    if flagged:
        return render_template(
            "result.html",
            output=f"Rejected due to exclusion: {disease}"
        )

    # ---------------- PATIENT INFO ----------------
    patient_info = f"""
Name: {name}
Address: {address}
Type: {claim_type}
Reason: {claim_reason}
Facility: {medical_facility}
Date: {date}
Amount: {total_claim_amount}
Description: {description}
"""

    # ---------------- LLM CALL ----------------
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=prompt_template)

    output = chain.run({
        "claim_approval_context": get_claim_approval_context(),
        "general_exclusion_context": get_general_exclusion_context(),
        "patient_info": patient_info,
        "medical_bill_info": bill_text,
        "max_amount": total_claim_amount
    })

    output = re.sub(r"\n", "<br>", output)

    return render_template("result.html", output=output)


# ===================== RUN =====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)