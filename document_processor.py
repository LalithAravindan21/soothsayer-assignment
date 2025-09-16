import pandas as pd
import pdfplumber
import io

class DocumentProcessor:
    def process_document(self, file_path, file_type):
        """Process uploaded documents and extract content"""
        if 'pdf' in file_type:
            return self._process_pdf(file_path)
        elif 'xlsx' in file_type or 'xls' in file_type:
            return self._process_excel(file_path)
        else:
            raise ValueError("Unsupported file type")
    
    def _process_pdf(self, file_path):
        """Extract text from PDF files"""
        text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
            return text
        except Exception as e:
            return f"Error processing PDF: {str(e)}"
    
    def _process_excel(self, file_path):
        """Extract data from Excel files"""
        df = pd.read_excel(file_path)
        return df.to_string()
