import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_model():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("❌ GROQ_API_KEY not found in .env file.")
    
    model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,
    api_key=api_key
)

    return model
