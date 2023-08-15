import requests
from datetime import datetime
import json
import os


exercise_headers = {
    'x-app-id': os.environ.get('APP_ID'),
    'x-app-key': os.environ.get('API_KEY'),
    'Content-Type': 'application/json',
}
exercise_params = {
    'query': input('Exercises you did today: '),
    'gender': '',                     #Enter your gender
    'weight_kg': 0,                   #Enter your weight
    'height_cm': 0,                   #Enter your height
    'age': 0                          #Enter your age
}

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
exercise_data = exercise_response.text
exercise_data = json.loads(exercise_data)

today_date = datetime.now().strftime(f'%Y/%m/%d')
today_time = datetime.now().strftime(f'%H:%M:%S')
exercise = exercise_data['exercises'][0]['name']
duration = exercise_data['exercises'][0]['duration_min']
calories = exercise_data['exercises'][0]['nf_calories']

SHEETY_TOKEN = os.environ.get('TOKEN')
add_data_params = {
    'workout': {
        'dat': today_date,
        'time': today_time,
        'exercise': exercise.title(),
        'duration': duration,
        'calories': calories
        }
    }

sheety_headers = {
    'Content-Type': 'application/json',
    'Authorization': SHEETY_TOKEN
    }

sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')
sheety_resposne = requests.post(url=sheety_endpoint, json=add_data_params, headers=sheety_headers)
print(sheety_resposne.text)