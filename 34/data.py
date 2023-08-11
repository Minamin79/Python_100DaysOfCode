import requests


parameters = {
    'amount': 10,
    'type': 'boolean'
}
response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()

n= 0 
question_data = []
for i in range(len(response.json()['results'])):
    question_data.append({'text': response.json()['results'][n]['question'], 
                          'answer': response.json()['results'][n]['correct_answer']})
    n += 1