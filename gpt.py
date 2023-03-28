import openai
import os
import pandas as pd
import time

# generate your api key on https://platform.openai.com/account/api-keys
# and set up your key in OS (https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
openai.api_key = os.environ['OPENAI_API_KEY']

domains = pd.read_csv('domains.csv')
start_time = time.time()
with open('test-first100.txt', 'w') as file:
    for i in range(0,100):
        URL = domains.iloc[i]['remote_hostname']
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
              {"role": "system", "content": "You are a network expert. Find out if the URL I provided is for tracking, marketing, advertising, analytics. Provide the response in JSON containing following fields: company, original URL, company website, description(30 to 100 words), result(yes/no)."},
              {"role": "user", "content": "For the description filed, I want you to describe the use of that URL, not the company."},
              {"role": "user", "content": "You don't need to provide explanations other than JSON"},
              {"role": "user", "content": URL}
            ],
            n=1,
            temperature=0.85
          )
        
        file.write(f'{str(completion.choices[0].message.content)}')
        file.write('\n')
        print(completion.choices[0].message.content)
  
end_time = time.time()
total = end_time - start_time
print('=============TIME USED: ' + str(total) + '=====================')

