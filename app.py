from chains import build_chain

def main():
    print("📧 Suspicious Email Detector (MailShield)")
    print("-----------------------------------------\n")

    email_text = input("Paste the suspicious email content:\n\n")

    chain = build_chain()
    print("\n🔍 Analyzing email...\n")

    response = chain.invoke({"email_text": email_text})

    print("🧠 Analysis Result:\n")
    print(response.content)
    print("\n✅ Done.")

if __name__ == "__main__":
    main()
