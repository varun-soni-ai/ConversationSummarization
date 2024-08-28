import streamlit as st
import json
from langchain_community.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page config and title
st.set_page_config(page_title="Conversation Summary Bot", page_icon="🤖")
st.title("Conversation Summary Bot 🤖")
st.text("This application accepts Json data containing messages and role(Prospect/Ambassador) and Genrate Conversation Summary.")

# File uploader
uploaded_file = st.file_uploader("Choose a JSON file", type="json")

@st.cache_resource
def load_summarizer():
    """Load the summarizer model and chain."""
    llm = OpenAI(temperature=0)
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    return chain

# Only process the file and generate summary when the user has uploaded a file
if uploaded_file is not None:
    # Load the summarizer
    summarizer = load_summarizer()
    
    # Load and parse JSON file
    conversation_data = json.load(uploaded_file)
    
    # Extract conversation from JSON
    conversation = ""
    for message in conversation_data:
        conversation += f"{message['role']}: {message['content']}\n\n"
    
    # Create a Document object
    document = Document(page_content=conversation)
    
    # Generate summary
    with st.spinner('Generating summary...'):
        summary = summarizer.run([document])  # Pass a list containing the document
    
    # Display summary
    st.subheader("Conversation Summary")
    st.write(summary)
else:
    st.info("Please upload a JSON file to generate a summary.")

# Add a footer
st.markdown("---")
st.markdown("Created with By Varun Soni ❤️ using Streamlit and LangChain")