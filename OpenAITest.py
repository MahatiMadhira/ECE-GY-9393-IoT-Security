import os
import openai

# generate your api key on https://platform.openai.com/account/api-keys
# and copy paste here
openai.api_key = ""

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "What is c.msn.com used for? Also show the sources"}
  ],
  n=3
)

print(completion.choices[0].message)
