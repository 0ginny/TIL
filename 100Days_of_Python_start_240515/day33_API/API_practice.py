import requests

# # get data from end point
# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# # response.raise_for_status() 아래와 같이 커스터마이징도 가능
# if response.status_code == 404 :
#     raise Exception('That resource does not exist.')
# if response.status_code == 401 :
#     raise Exception('You are not authorised to access this data .')
#
# data = response.json()
# print(data)

# 입력 파라미터가 필요할 때
parameter = {
    'lat' : 35.234,
    'lng' : 140.2434,
    'formatted' : 0
}

response = requests.get(url=" https://api.sunrise-sunset.org/json", params= parameter)
response.raise_for_status()
data = response.json()['results']
for key in data:
    print(key, data[key])