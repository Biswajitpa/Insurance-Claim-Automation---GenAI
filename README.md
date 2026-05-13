# AI Powered Automated Claims Processing (ClaimTrackr)
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=28&duration=4000&color=00C2FF&center=true&vCenter=true&width=900&lines=Insurance+Claim+Tracker;AI+Powered+Claim+Automation+System;Fast+%7C+Secure+%7C+Smart+Processing;Built+with+Flask+%2B+OpenAI+%2B+LangChain" />
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:141e30,100:243b55&height=200&section=header&text=Insurance%20Claim%20Tracker&fontSize=40&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=20&duration=3500&color=00F5FF&center=true&vCenter=true&width=900&lines=AI+Powered+Insurance+Claim+Automation+System;Simplifying+Claim+Verification+%7C+Fraud+Detection+%7C+Approval;Using+Artificial+Intelligence+%2C+NLP+%26+Automation" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Flask-Web%20App-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenAI-GPT%203.5-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LangChain-AI%20Workflow-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FAISS-Vector%20Search-orange?style=for-the-badge" />
</p>

---

<p align="center">
  <img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="500"/>
</p>

---

## Problem Statement: 
- Time-consuming and Error-prone Insurance Claim Processes
- Efficient and accurate insurance claim processing is vital in the finance and banking industry. It impacts customer satisfaction, operational costs, and regulatory compliance. 
However, this task is often hindered by complexity and vast amounts of data, making it time-consuming and prone to errors. This tool provides a solution by simplifying and automating insurance claim processing.

## Context
Leveraging the power of machine learning, natural language & Gen AI, this tool automates the traditionally manual insurance claim processing procedure. 
- Implementation of AI and Generative AI will enhance data analysis and predictive capabilities
- AI will provide deeper insights, improve accuracy, and streamline reporting processes
- Predictive features will enable proactive decision-making based on anticipated impact fluctuations.

## Objectives
Develop a chatbot using AI to assist the process of claim processing, and approval.
- 	Real-time Support: Offer an executive summary of the claims, and also provide whether the claims are valid or not.
- 	Educational Resource: Share knowledge on membership handbooks

![image](https://github.com/user-attachments/assets/b480145b-851d-44c4-84a3-b106b7136596)

## How it works
Leveraging the power of artificial intelligence and machine learning, ClaimTrackr automates the traditionally manual insurance claim processing procedure. Here’s a comparison of the time required for each task with and without ClaimTrackr Flow:
 
![image](https://github.com/user-attachments/assets/6a952a83-acfc-4110-9f2a-2e66aad049e3)

## Key Inputs
For this particular project, we would need the below key inputs:
•	Medical Insurance Company’s handbook & necessary documents
•	Previous Claim details
•	Claimant (Policy Holder) details – Personal, Medical records, and bills (if any)

## Architecture
  
![image](https://github.com/user-attachments/assets/0d269565-1555-4911-a0d3-36ecec431415)

Step 1: Data Collection and Exploratory Data Analysis
ClaimTrackr initiates the insurance claim processing by automatically collecting the relevant data such as customer records, external data sources, medical records, policyholder information, and government data, ensuring that all information is accurate and up to date. Once the data is validated, ClaimTrackr performs an automated EDA, revealing helpful insights within the gathered data. This step is pivotal in identifying patterns, anomalies, and historical trends that can greatly enhance the overall efficiency of the insurance claim processing procedure.

Step 2: Embeddings Generation
In this stage, textual data is converted into numerical embeddings using advanced techniques. These embeddings capture the semantic relationships within the data, enabling ClaimTrackr to retrieve and analyze information efficiently. The generated embeddings simplify claim information assessment against policy terms and conditions, medical records, and external data to determine claim validity and calculate settlement amounts.

Step 3: Query Execution and Report Generation
Once a claim is prepared for processing, ClaimTrackr utilizes the OpenAI Language Model (LLM) to evaluate the insurance claim status. A detailed report is promptly generated in response to the user’s query, providing essential information about the claim, its assessment, and the proposed settlement. The report generation process is characterized by its high efficiency and consistency, guaranteeing the inclusion of all pertinent information.
Furthermore, with the help of embeddings, the OpenAI LLM is capable of offering deep insights, conducting a thorough review to detect any potential signs of fraud, and providing actionable recommendations for the claim.

Step 4: Parsing and Final Output Generation
After the report is generated by the LLM, ClaimTrackr employs a parsing technique to refine the report and extract useful insights. ClaimTrackr’s role in this phase involves delivering comprehensive, well-organized data that ultimately speeds up the approval process and reduces the time needed for claim settlement.

## Product Demo

![image](https://github.com/user-attachments/assets/e680e2f6-127c-4bee-9cef-d39b303c1a0e)

 ## Product Report
Final report is generated with the final verdict whether the Insurance claim was valid or rejected, rejection criterias were claimed amount vs allowed amount, name validations and disease validation under the Exclusion list of the medical handbook.
