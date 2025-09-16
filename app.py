import streamlit as st
import pandas as pd
from pathlib import Path
from document_processor import DocumentProcessor
from qa_system import QASystem
import tempfile

def main():
    st.title("Financial Document Q&A Assistant")
    
    # Initialize session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'document_content' not in st.session_state:
        st.session_state.document_content = None
    
    # Sidebar for document upload
    with st.sidebar:
        st.header("Upload Documents")
        uploaded_file = st.file_uploader(
            "Choose a financial document (PDF or Excel)",
            type=['pdf', 'xlsx', 'xls']
        )
        
        if uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                file_path = tmp_file.name
                
            processor = DocumentProcessor()
            content = processor.process_document(file_path, uploaded_file.type)
            st.session_state.document_content = content
            st.success("Document processed successfully!")
    
    # Main chat interface
    st.header("Ask Questions About Your Financial Data")
    
    # Display chat history
    for message in st.session_state.chat_history:
        role = message["role"]
        content = message["content"]
        with st.chat_message(role):
            st.write(content)
    
    # Chat input
    if prompt := st.chat_input("Ask a question about your financial data"):
        if not st.session_state.document_content:
            st.error("Please upload a document first!")
            return
        
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        # Get AI response
        qa_system = QASystem()
        response = qa_system.get_response(prompt, st.session_state.document_content)
        
        # Add AI response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        # Rerun to update chat display
        st.rerun()

if __name__ == "__main__":
    main()
