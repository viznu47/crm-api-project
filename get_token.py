import json, requests
from dotenv import load_dotenv
import os
# to get token for authorization
def get_token(email_address, password):
    payload = {
        "email_address": email_address,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post("https://devapi.4dcrm.com/login", json=payload, headers=headers) # token API
    if response.status_code == 200:
        data = response.json()
        token = data.get("token")
        return token
    else:
        print("Failed to get token. Status code:", response.status_code)
        return None

# hide the credentials here

email = os.getenv("email")
password = os.getenv("password")

token = get_token(email, password)
