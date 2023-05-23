import openai

openai.api_key = open('secret_key.txt', 'r').read().strip('\n')

def generate_message(user_input):
    messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": user_input}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']