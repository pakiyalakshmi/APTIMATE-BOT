from nltk.tokenize import sent_tokenize
from nltk import download as nltk_download
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import streamlit as st
import langchain

from chat import process_text
langchain.verbose = False

# Load env variables
load_dotenv()

# Download NLTK punkt tokenizer if not already downloaded
try:
    nltk_download('punkt')
except LookupError:
    pass
 
def tokenize_sentences(text):
    return sent_tokenize(text)

def ask_question(sentences, question):
    matching_sentences = []
    for sentence in sentences:
        if question.lower() in sentence.lower():
            matching_sentences.append(sentence)
    return matching_sentences

def main():
    st.title("Chat with my PDF")

    pdf = st.file_uploader("Upload your PDF File", type="pdf")

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        # Store the pdf text in a variable
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        sentences = tokenize_sentences(text)

        question = st.text_input('Ask question to PDF...')

        cancel_button = st.button('Cancel')

        if cancel_button:
            st.stop()

        if question:
            matching_sentences = ask_question(sentences, question)
            if matching_sentences:
                st.write("Matching sentences found:")
                for sentence in matching_sentences:
                    st.write("-", sentence)
            else:
                st.write("No matching sentences found.")

if _name_ == "_main_":
    main()
