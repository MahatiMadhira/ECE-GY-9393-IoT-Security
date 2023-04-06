import openai
import os
import pandas as pd
import time
import json
import prompts


# set up API key in OS (https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
openai.api_key = os.environ["OPENAI_API_KEY"]

# prepare dataframe
domains = pd.read_csv("./data/domains.csv")
domains.insert(len(domains.columns), 'company', "")
domains.insert(len(domains.columns), 'company_website', "")
domains.insert(len(domains.columns), 'result', "")

total_count = len(domains)  # length of the dataset
step = 200
temperature = 1
prompt = prompts.prompt3

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

for start in range(0, total_count, step):

    start_time = time.time()

    for i in range(start, min(start + step, total_count)):
        print('====' + str(i) + '====')
        completion = None
        try:
            URL = domains.iloc[i]["remote_hostname"]
            completion = gpt_query(URL, temperature, prompt)
        except Exception as e:
            completion = gpt_query(URL, temperature, prompt)
            continue

        # convert str to json
        print(completion.choices[0].message.content)
        try:
            resp = json.loads(completion.choices[0].message.content)
            res = ""
            if 'result' in resp:
                res = resp['result']
            else:
                res = resp['purpose']
            
            # cdn fine-grained
            if 'CDN' in res or 'cdn' in res:
                pass

            domains.loc[i, ['company','company_website','result']] = [resp['company'], resp['company_website'], res]
        except Exception:
            print('=======================' + str(i) + ' is wrong =======================')
            continue

    filename = "./data/full/haoran/prompt3/answers_" + str(start) + ".csv"

    domains.loc[list(range(start, min(start + step, total_count)))].to_csv(filename)

    end_time = time.time()
    time_used = end_time - start_time
    print("=============TIME USED: " + str(time_used) + "=====================")


