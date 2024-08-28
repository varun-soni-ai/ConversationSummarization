import streamlit as st
import json
from langchain_community.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
st.title("Conversation Summary Bot")

uploaded_file = st.file_uploader("Choose a JSON file", type="json") 
if uploaded_file is not None:
    
    conversation_data = json.load(uploaded_file) # Load and parse JSON file
    conversation = "" # Extract conversation from JSON
    for message in conversation_data:
        conversation += f"{message['role']}: {message['content']}\n\n"
    
    document = Document(page_content=conversation) # Create a Document object
    
    llm = OpenAI(temperature=0)
    chain = load_summarize_chain(llm, chain_type="map_reduce")# Create LangChain summarizer
    
    # Generate summary
    summary = chain.run([document])  # Pass a list containing the document
    
    # Display summary
    st.subheader("Conversation Summary")
    st.write(summary)