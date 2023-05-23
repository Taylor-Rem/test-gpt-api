import openai

openai.api_key = open('secret_key.txt', 'r').read().strip('\n')

def chat():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    while True:
        user_message = input("You: ")

        if user_message.lower() == "quit":
            break

        messages.append({"role": "user", "content": user_message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        assistant_message = response.choices[0].message['content']

        print("ChatGPT: ", assistant_message)

        messages.append({"role": "assistant", "content": assistant_message})

if __name__ == '__main__':
    chat()