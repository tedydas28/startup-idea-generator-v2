import openai
import os
from dotenv import load_dotenv

# Load the .env file locally (ignored on Streamlit Cloud)
load_dotenv()

# Access the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
