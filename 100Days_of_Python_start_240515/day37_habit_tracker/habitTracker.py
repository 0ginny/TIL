import requests
import json
import datetime as dt
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
# print(f'{graph_endpoint}/{graph_config["id"]}.html')

# 3. post pixel
post_endpoint = f"{graph_endpoint}/{graph_config['id']}"
# print(post_endpoint)
# datetime format : https://chancoding.tistory.com/222
date_now = dt.datetime.now().strftime("%Y%m%d")
# print(date_now)
post_config = {
    "date" :date_now,
    "quantity" : "30",
}

# response = requests.post(url=post_endpoint,json=post_config,headers=headers)
# print(response.text)

# 4. put(update) data
edit_date = date_now
update_endpoint = f'{post_endpoint}/{edit_date}'

update_config = {
    "quantity" : "350"
}

# response = requests.put(url=update_endpoint,json=update_config,headers=headers)
# print(response.text)


# 5. delete data
delete_date = date_now
delete_endpoint = f'{post_endpoint}/{delete_date}'


response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)