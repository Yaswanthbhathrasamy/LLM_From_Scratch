# streamlit_app.py
import streamlit as st
from chains import build_chain

def main():
    st.set_page_config(page_title="💻 Simple Code Generator", layout="centered")

    st.title("💡 Simple Code Generator")
    st.write("Generate code for any programming task using an LLM!")

    program_type = st.text_input("Enter the programming language / program type (e.g., 'Python script', 'Java class')")
    topic = st.text_input("Enter the topic (e.g., 'Bubble Sort', 'Web Scraper')")

    if st.button("🚀 Generate Code"):
        if not program_type or not topic:
            st.warning("⚠️ Please fill in both fields before generating.")
        else:
            with st.spinner("Generating code... Please wait..."):
                chain = build_chain()
                response = chain.invoke({"program_type": program_type, "topic": topic})
                st.success("✅ Code generated successfully!")
                st.code(response.content, language="python")

if __name__ == "__main__":
    main()
