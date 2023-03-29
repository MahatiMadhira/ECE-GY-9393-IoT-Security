import openai
import os
import pandas as pd
import time

# generate your api key on https://platform.openai.com/account/api-keys
# and set up your key in OS (https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
openai.api_key = os.environ['OPENAI_API_KEY']

domains = pd.read_csv('domains.csv')
total_count = domains.count()
step = 300 # 300 domains per iteration
start = 0

start_time = time.time()

while start <= total_count:
  end = min(start + step, total_count)
  filename = "result-" + start + "-" + end + ".txt"
  try:
    with open(filename, 'w') as file:
      for i in range(start, end):
          URL = domains.iloc[i]['remote_hostname']
          completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[
                {"role": "system", "content": "You are a network expert. Find out the purpose of the provided URL (tracking, marketing, advertising, analytics, CDN, static server, DNS, first-party host).  Response in JSON containing following fields: company, original URL, company website, result. Respond in JSON only."},
                {"role": "user", "content": URL}
              ],
              n=1,
              temperature=0.85
            )
          
          file.write(f'{str(completion.choices[0].message.content)}')
          file.write('\n')
          print(completion.choices[0].message.content)
  except:
     print('error occured at ' + start + ' ' + end)
  start = end
  
end_time = time.time()
time_used = end_time - start_time
print('=============TIME USED: ' + str(time_used) + '=====================')

