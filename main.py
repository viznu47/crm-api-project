from get_token import *
import requests, json
from bs4 import BeautifulSoup
from pprint import pprint
from transformers import pipeline
sent_pipeline = pipeline("sentiment-analysis") #, model="roberta-base")
import warnings, logging
from nltk.tokenize import WhitespaceTokenizer
tk = WhitespaceTokenizer()
     
# if token:
#     print("Token:", token)

# API for thread from https://devapi.4dcrm.com/explorer/#/
thread_url = "https://devapi.4dcrm.com/threads?filter=%7B%0A%20%20%0A%20%20%22fields%22%3A%20%7B%0A%20%20%20%20%22id%22%3A%20true%2C%0A%20%20%20%20%22threadContent%22%3A%20true%2C%0A%20%20%20%20%22threadType%22%3A%20true%2C%0A%20%20%20%20%22incidentId%22%3A%20true%2C%0A%20%20%20%20%22createdBy%22%3A%20true%2C%0A%20%20%20%20%22createdDatetime%22%3A%20true%2C%0A%20%20%20%20%22updatedBy%22%3A%20true%2C%0A%20%20%20%20%22updatedDatetime%22%3A%20true%2C%0A%20%20%20%20%22sendResponse%22%3A%20true%2C%0A%20%20%20%20%22sendGridMessageID%22%3A%20true%0A%20%20%7D%0A%7D"
headers = {
    "Authorization": "Bearer " + token,
    "x-sessionid-s" : "3",
    "x-sessionid-t" : "1",
}
r = requests.get(thread_url, headers=headers)
data = r.json()

# fn to extract the message from html content 
def extractMessage(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    paragraphs = soup.find_all('p')

    message = ''
    for paragraph in paragraphs:
        message += paragraph.get_text().strip() + ' '

    return message.strip()

# print(json.dumps(data, indent=4, sort_keys=True))

# storing the cleaned messages in an array
thread_content = [extractMessage(i['threadContent']) for i in data]


# new_content = [text[:512] for text in thread_content]
# sentiment =[sent_pipeline(i) for i in thread_content]
sentiment = []
for i in range(len(thread_content)):
    try:
        sentiment.append(sent_pipeline(thread_content[i])[0]['label'])
    except Exception:
        sentiment.append("Too long")
        # print(f"{e} error at {i}th index")

print(*sentiment, sep="\n")
print(len(sentiment))
print(sentiment.index("Too long")) # 200 

