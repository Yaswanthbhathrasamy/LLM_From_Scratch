from prompts import email_prompt
from models import get_model

def build_chain():
    """Builds the LangChain pipeline for email analysis."""
    model = get_model()
    chain = email_prompt | model
    return chain
