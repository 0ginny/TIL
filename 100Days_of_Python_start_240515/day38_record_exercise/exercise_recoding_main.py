import json
import requests as rq

MY_WEIGHT = 75
MY_HEIGHT = 175.6
MY_AGE = 27

with open('record_exercise_secret.json') as file :
    secret_data = json.load(file)
    NUTRITION_ID = secret_data['nutrition_id']
    NUTRITION_KEY = secret_data['nutrition_key']



# 1. nutrition data 불러오기

NUTRITION_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# Nutritional api doc : https://docx.syndigo.com/developers/docs/natural-language-for-exercise

HEADER= {
    'Content-Type': 'application/json',
    'x-app-id': NUTRITION_ID,
    'x-app-key': NUTRITION_KEY
  }

CONFIG = {
    'query' : input("Tell me which exercises you did : "),
    'weight_kg':MY_WEIGHT,
    'height_cm':MY_HEIGHT,
    'age':MY_AGE
}

response = rq.post(url=NUTRITION_ENDPOINT,json=CONFIG,headers=HEADER)
print(response.text)


