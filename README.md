🔑 API Key Setup

This project requires an OpenAI API key to run.

Sign up at OpenAI
 and create an API key from your API Keys Dashboard
.

Inside the project folder, create a hidden directory named .streamlit (if it doesn’t already exist):

mkdir .streamlit


Inside .streamlit, create a file named secrets.toml and add your API key like this:

OPENAI_API_KEY = "your_api_key_here"


Run the Streamlit app:

streamlit run app.py
