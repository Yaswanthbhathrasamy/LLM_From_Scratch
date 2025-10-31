from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

def get_model():
    """Initialize and return the Groq LLM model."""
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("⚠️ GROQ_API_KEY not found in .env file.")
    
    model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        max_tokens=512,
        api_key=groq_api_key
    )
    return model
