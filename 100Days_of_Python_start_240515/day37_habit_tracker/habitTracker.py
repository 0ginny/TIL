import requests
import json

# api doc : https://docs.pixe.la/

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

# response = requests.post(url=pixela_url,json=user_params)

# 2. create graph
graph_endpoint = f"{pixela_url}/{data['username']}/graphs"

graph_config = {
    "id" : data["graph_id"],
    "name" : "Studying Graph",
    "unit" : "min",
    "type" : "int",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN":data["token"]
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

# 생성된 주소
print(f'{graph_endpoint}/{graph_config["id"]}.html')