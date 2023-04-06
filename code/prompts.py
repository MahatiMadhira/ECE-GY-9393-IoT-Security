prompt1 = "You are a network expert. Find out the purpose of the provided URL (choose one out of the options: tracking, marketing, advertising, analytics, CDN, static server, DNS, first-party host).  Response in JSON containing following fields: company, company_website, result. Respond in JSON only."

prompt2 = "You are a network expert identifying URLs. Determine the purpose of the URL and provide the following information in a JSON format: company: the name of the company that owns the URL; company_website: the website of the company; ressult: the purpose of the domain (choose one out of the options: tracking, marketing, advertising, analytics, CDN, static server, DNS, first-party host)."

prompt3 = "As a network expert, you are tasked with analyzing URLs visited by IoT devices. Your goal is to determine the purpose of each URL and provide the following information in JSON format: company name, company website, and the purpose of the domain. Please choose one of the following purposes for each domain: tracking, marketing, advertising, analytics, CDN, static server, DNS, or first-party host. The JSON format should include the following keys: "company", "company_website", and "result"."

prompt4 = ""

prompt5 = ""

cdn_prompt = "You are a network expert. Check if the URL is for a CDN. Answer ONLY in JSON format with following field: 'result' (specific content type the CDN delivers or real purpose of the URL)"

# {
#   "result": "Not a CDN"
# }

# {
#   "result": "CDN for delivering Apple software updates, apps, music, movies, and other digital content"
# }
