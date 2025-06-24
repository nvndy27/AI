import google.generativeai as genai

# Thay bằng API key bạn lấy ở https://makersuite.google.com/app/apikey
genai.configure(api_key="AIzaSyDbIhIxhwHCOZW59c89kxQhPezi7hl79EA")

# Dùng đúng API model từ v1: Gemini 1.5 Pro hoặc Gemini 1.0 Pro
model = genai.GenerativeModel(model_name="gemini-1.5-pro")  # hoặc "gemini-pro"

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

def main():
    print("Ask me anything (type 'bye' to exit).")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break
        reply = ask_gemini(user_input)
        print("Bot:", reply)

if __name__ == "__main__":
    main()
