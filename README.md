# ConversationSummarization

**Overview**: This Streamlit application creates a conversation summary bot using LangChain and OpenAI's language model. It allows users to upload a JSON file containing a conversation, processes the conversation, and generates a summary using natural language processing techniques.

> Components and Libraries Used:

>> **Streamlit**: For creating the web application interface

>> **JSON**: For parsing the uploaded JSON file

>> **LangChain**: For creating and running the summarization chain

>> **OpenAI**: As the language model for summarization

>> **dotenv**: For loading environment variables

> Key Functions and Their Roles: a. File Upload:
- Uses Streamlit's file_uploader to allow users to upload a JSON file

> b. JSON Processing:
- Parses the uploaded JSON file
- Extracts conversation data from the JSON structure

> c. Conversation Formatting:
- Formats the extracted conversation into a string
- Creates a LangChain Document object from the formatted conversation

> d. Summarization:
- Utilises OpenAI's language model through LangChain
- Creates a summarization chain using the "map_reduce" strategy
- Generates a summary of the conversation

> e. Display:
- Shows the generated summary in the Streamlit interface

> Workflow:
- The user uploads a JSON file containing a conversation
- The application reads and processes the JSON file
- The conversation is extracted and formatted
- A LangChain summarization pipeline is created
- The conversation is summarised using the OpenAI model
- The summary is displayed to the user

> **Requirements**:
- Python 3.6+
- Streamlit
- LangChain
- OpenAI API key (stored in an environment variable)
- JSON-formatted conversation data

> **Environment Setup:**
- The application uses dotenv to load environment variables
- The OpenAI API key should be stored in a .env file or set as an environment variable

> **Model Options**: While this code uses OpenAI's model, LangChain supports various language models. Alternatives could include:
- Hugging Face models 
- Google's PaLM
- Anthropic's Claude
- Cohere's language models


To use a different model, you would need to import the appropriate LangChain integration and modify the llm initialization.

- Hugging Face model: You'll need to set the HUGGINGFACEHUB_API_TOKEN in your environment variables.
- Google PaLM: You'll need to set the GOOGLE_PALM_API_KEY in your environment variables.
- Anthropic's Claude: You'll need to set the ANTHROPIC_API_KEY in your environment variables.
- Cohere: You'll need to set the COHERE_API_KEY in your environment variables.

Note : To implement any of these changes, you would replace the OpenAI model initialization in your original code:

Remember to install the necessary packages for each model. You can do this using pip:
- pip install langchain-community
- pip install huggingface_hub  # for HuggingFace
- pip install google-api-python-client  # for Google PaLM
- pip install anthropic  # for Anthropic
- pip install cohere  # for Cohere


**Customization Possibilities**:
- Adjust the summarization parameters (e.g., max_tokens, temperature)
- Implement different summarization strategies (e.g., "stuff" or "refine" instead of "map_reduce")
- Add error handling for file processing and API calls
- Enhance the UI with additional Streamlit components

**Limitations**:
Depends on the structure of the input JSON file
Requires an active internet connection for API calls to OpenAI
Summary quality depends on the capabilities of the chosen language model

