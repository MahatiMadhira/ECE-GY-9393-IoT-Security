import openai
import os
import pandas as pd

# generate your api key on https://platform.openai.com/account/api-keys
# and set up your key in OS (https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
openai.api_key = os.environ['OPENAI_API_KEY']

domains = pd.read_csv('domains.csv')

with open('test-first100.txt', 'w') as file:
    for i in range(0,10):
        URL = domains.iloc[i]['remote_hostname']
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
              {"role": "system", "content": "You are a network expert. Find out if the URL I provided is for tracking, marketing, advertising, analytics. Provide the response in JSON containing following fields (for result field, say yes if the URL is for tracking, marketing, advertising, analytics): company, original URL, company website, descriptions, result, source links."},
              {"role": "user", "content": URL}
            ],
            n=1,
            temperature=0.8
          )
        
        file.write(f'{str(completion.choices[0].message.content)}')
        file.write('\n')
        print(completion.choices[0].message.content)
  


