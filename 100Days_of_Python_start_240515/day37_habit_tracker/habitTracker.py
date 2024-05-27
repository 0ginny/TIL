import requests
import json

# 1. create user
pixela_url = "https://pixe.la/v1/users"

with open('secret.json') as file:
    data = json.load(file)

user_params = {
    "token": data['token'],  # 임의로 정하는 거야ㅑ.
    "username": data['username'],
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_url,json=user_params)
print(response.text)