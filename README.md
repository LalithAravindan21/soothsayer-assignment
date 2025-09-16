📘 Financial Document Q&A Assistant
🎯 Problem Statement

Develop a web application that can process financial documents (PDF and Excel formats) and provide an interactive question-answering system for users to query financial data using natural language.

The application extracts relevant financial information from uploaded documents and responds to user questions about revenue, expenses, profits, and other financial metrics.

✨ Features
📂 Document Processing

Upload PDF and Excel financial statements

Extract text and tabular data

Supports Income Statements, Balance Sheets, Cash Flow Statements

Handles different layouts and formats

💬 Question-Answering

Ask natural language questions about your financial data

Extracts and presents specific metrics (e.g., revenue, liabilities, equity, etc.)

Supports follow-up conversational queries

🖥️ User Interface

Built with Streamlit

Sidebar for document uploads

Interactive chat-style Q&A interface

Clear feedback and readable output

⚙️ Technical Implementation

Streamlit for UI

LangChain + OpenAI GPT for Q&A

pdfplumber and pandas for document parsing

Local execution (no cloud deployment required)

Error handling and user feedback

🚀 Getting Started
🔧 Prerequisites

Make sure you have installed:

Python 3.9+

Pip

Clone the repository:

git clone https://github.com/LalithAravindan21/soothsayer-assignment.git
cd soothsayer-assignment


Install dependencies:

pip install -r requirements.txt

🔑 API Key Setup

This project requires an OpenAI API Key.

Sign up at OpenAI
 and create an API key from your API Keys Dashboard
.

Inside the project folder, create a hidden directory named .streamlit (if it doesn’t already exist):

mkdir .streamlit


Inside .streamlit, create a file named secrets.toml and add your key like this:

OPENAI_API_KEY = "your_api_key_here"


⚠️ Important: Do not share or commit your API key.
The .streamlit/secrets.toml file is in .gitignore, so it won’t be pushed to GitHub.

▶️ Running the Application

Start the app with:

streamlit run app.py


Open your browser at http://localhost:8501
.

📤 Submission Requirements

Duration: 4 days

Code is publicly available on GitHub

Includes README.md with setup and usage instructions

✅ Success Criteria

The application demonstrates:

Uploading and processing financial documents

Extracting meaningful data

Answering basic financial queries through a chat interface
