import requests

# get data from end point
response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# response.raise_for_status() 아래와 같이 커스터마이징도 가능
if response.status_code == 404 :
    raise Exception('That resource does not exist.')
if response.status_code == 401 :
    raise Exception('You are not authorised to access this data .')

data = response.json()
print(data)