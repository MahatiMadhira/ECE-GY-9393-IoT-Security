# ECE GY 9393 IoT Security Project
Haoran Wang | Mahati Madhira

## Structure
```
├───code --------------------- Python scripts                        
│   └───jupyter -------------- Jupyter notebook for data preprocessing
└───data --------------------- data in csv files
    ├───CDN ------------------ for CDN records analysis
    └───full ----------------- full dataset query results
        ├───haoran  
        │   ├───prompt1
        │   └───prompt2
        └───mahati
            ├───prompt3
            └───prompt4
```

## GPT Processing
* Split dataset into pieces (200 per iteration)
* Results in JSON format, save to csv files

## Validating
- manually sample and check
- interest points (some interesting URLs)
- CDN fine grind

## Comparing different prompts
1 initial prompt (prompt1) + 4 different of prompts
### Initial prompt
> You are a network expert. Find out the purpose of the provided URL (choose one out of the options: tracking, marketing, advertising, analytics, CDN, static server, DNS, first-party host).  Response in JSON containing following fields: company, company_website, result. Respond in JSON only.
### Haoran
- prompt 2: paraphrased prompt1
> You are a network expert identifying URLs. Determine the purpose of the URL and provide the following information in a JSON format: company: the name of the company that owns the URL; company_website: the website of the company; ressult: the purpose of the domain (choose one out of the options: tracking, marketing, advertising, analytics, CDN, static server, DNS, first-party host).
- prompt 3
### Mahati
- prompt 4
- prompt 5