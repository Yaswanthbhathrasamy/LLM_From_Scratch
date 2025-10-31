from langchain_core.prompts import ChatPromptTemplate

system_prompt = """
You are a cybersecurity analyst specialized in detecting phishing and suspicious emails.
Analyze the given email content and classify it as one of:
- Legitimate
- Spam
- Phishing

You must also explain the reasoning clearly and provide a short safety tip.
Never render links or click them.
"""

user_prompt = """
Email content:
{email_text}
"""

email_prompt = ChatPromptTemplate([
    ("system", system_prompt),
    ("user", user_prompt)
])
