import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class QASystem:
    def __init__(self):
        try:
            self.api_key = st.secrets["OPENAI_API_KEY"]
            # Use GPT-4o-mini (fast, cost-efficient) or GPT-4 if needed
            self.llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0,
                openai_api_key=self.api_key
            )
        except Exception as e:
            st.error(f"Error initializing OpenAI LLM: {str(e)}")
            self.llm = None
            
    def get_response(self, question, context):
        """Generate response for user questions"""
        if self.llm is None:
            return "Error: LLM is not properly initialized. Please check your API key configuration."
        
        try:
            template = """
            You are a financial assistant. Use the provided financial document text to answer questions.

            Context:
            {context}

            Question: {question}

            Answer clearly and concisely:
            """
            prompt = PromptTemplate(template=template, input_variables=["context", "question"])
            
            formatted_prompt = prompt.format(context=context[:6000], question=question)  
            # Limit context length for safety
            
            response = self.llm.predict(formatted_prompt)
            return response.strip()
        
        except Exception as e:
            return f"Error generating response: {str(e)}"
