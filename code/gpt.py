import openai
import os
# generate your api key on https://platform.openai.com/account/api-keys
# and set up your key in OS (https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
openai.api_key = os.environ["OPENAI_API_KEY"]

def gpt_query(URL, temperature, prompt):
    completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": prompt,
                    },
                    {"role": "user", "content": URL},
                ],
                n=1,
                temperature=temperature,
            )
    return completion