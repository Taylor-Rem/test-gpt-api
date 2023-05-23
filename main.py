import openai

openai.api_key = open('secret_key.txt', 'r').read().strip('\n')

print(openai.api_key)