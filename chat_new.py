from openai import OpenAI

# Initialize OpenAI client
API_KEY = "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"
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

def get_ai_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("請輸入您的問題，輸入 'exit' 退出程式。")
    while True:
        user_input = input("您: ")
        if user_input.lower() == 'exit':
            print("再見！")
            break

        # Use OpenAI API to generate a response
        response = get_ai_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
