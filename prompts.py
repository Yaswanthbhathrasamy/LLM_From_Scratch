from langchain_core.prompts import ChatPromptTemplate

system_msg = """
You are a code-generation assistant. When given a programming language and a topic,
you must produce only the requested program's source code — nothing else.

Rules:
1. Output raw source code in the requested language.
2. Add minimal inline comments.
3. No explanations, markdown, or text outside of the code.
"""

user_msg = "Generate a {program_type} that implements: {topic}. Include helpful comments."

prompt_template = ChatPromptTemplate([
    ("system", system_msg),
    ("user", user_msg)
])
