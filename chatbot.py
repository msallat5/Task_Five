import anthropic

# Set your Claude API key
ANTHROPIC_API_KEY = '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'

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def chat_with_claude(prompt):
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",  # Adjust based on the actual model name
            max_tokens=1000,
            temperature=0,
            system="You are a helpful assistant.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )
        return message['completion'].strip()
    except Exception as e:
        error_message = f"Error: {str(e)}"
        if "credit balance is too low" in error_message:
            return "Your credit balance is too low to access the Claude API. Please go to Plans & Billing to upgrade or purchase credits."
        return error_message

def main():
    while True:
        print("Enter 1 to start the chatbot or 0 to exit.")
        start_input = input("Your choice: ")

        if start_input == '0':
            print("Exiting the chatbot. Goodbye!")
            break
        elif start_input == '1':
            print("Chatbot: Hello! How can I assist you today?")
            while True:
                user_input = input("You: ")
                if user_input == '0':
                    print("Chatbot: Goodbye!")
                    break

                response = chat_with_claude(user_input)
                print(f"Chatbot: {response}")
        else:
            print("Invalid input. Please enter 1 to start or 0 to exit.")

if __name__ == "__main__":
    main()
