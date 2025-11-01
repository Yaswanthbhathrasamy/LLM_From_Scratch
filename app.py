from chains import build_chain

def main():
    print("=== Simple Code Generator ===")
    program_type = input("Enter the programming language / program type (e.g., 'Python script', 'Java class'): ")
    topic = input("Enter the topic (e.g., 'Bubble Sort', 'Web Scraper'): ")

    print("\nGenerating code... Please wait...\n")
    chain = build_chain()
    response = chain.invoke({"program_type": program_type, "topic": topic})
    print(response.content)

if __name__ == "__main__":
    main()
