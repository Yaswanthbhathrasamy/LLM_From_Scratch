from langchain_core.prompts import ChatPromptTemplate
from models import get_model

def build_chain():
    model = get_model()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that generates code."),
        ("user", "Generate a {program_type} for the topic: {topic}. Include helpful comments.")
    ])

    chain = prompt | model
    return chain
