import json
import requests as rq
import datetime as dt
import googletrans

translater = googletrans.Translator()

MY_WEIGHT = 75
MY_HEIGHT = 175.6
MY_AGE = 27

with open('record_exercise_secret.json') as file:
    secret_data = json.load(file)
NUTRITION_ID = secret_data['nutrition_id']
NUTRITION_KEY = secret_data['nutrition_key']
sheety_userCode = secret_data['sheety_userCode']
sheety_projectName = secret_data['sheety_projectName']
sheety_sheetName = secret_data['sheety_sheetName']

# 1. nutrition data 불러오기

NUTRITION_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# Nutritional api doc : https://docx.syndigo.com/developers/docs/natural-language-for-exercise

HEADER = {
    'Content-Type': 'application/json',
    'x-app-id': NUTRITION_ID,
    'x-app-key': NUTRITION_KEY
}

CONFIG = {
    'query': translater.translate(input("금일 무슨 운동을 했는지 적어주세요 : "),dest='en').text,
    'weight_kg': MY_WEIGHT,
    'height_cm': MY_HEIGHT,
    'age': MY_AGE
}

rq_nutrition_excercise = rq.post(url=NUTRITION_ENDPOINT, json=CONFIG, headers=HEADER)
nutrition_data = rq_nutrition_excercise.json()

# 2. sheety 로 google sheet 수정하기
# sheety url : https://dashboard.sheety.co/login
SHEETY_ENDPOINT = f"https://api.sheety.co/{sheety_userCode}/{sheety_projectName}/{sheety_sheetName}"
print(SHEETY_ENDPOINT)

now = dt.datetime.now()
now_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%H:%M:%S")

# "workouts" 에서 s를 빼야해. 자연어 인식인가? 중복이 아닌 글자로 해야해.
for exercise in nutrition_data["exercises"]:
    SHEETY_JSON = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    rq_sheety_get = rq.post(url=SHEETY_ENDPOINT, json=SHEETY_JSON)
    print(rq_sheety_get.text)

