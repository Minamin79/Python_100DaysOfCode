import requests
from datetime import datetime


USERNAME = 'mina0mina'
TOKEN = 'Minaewrgwegw5gliweflaslvmlar'
GRAPH_ID = 'graph1'
header = {'X-USER-TOKEN': TOKEN}

# ---------------------------- CREATE A USER ------------------------------- #
pixela_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
pixela_endpoint = 'https://pixe.la/v1/users'
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)


# ---------------------------- MAKE A GRAPH ------------------------------- #
graph_params = {
    'id': GRAPH_ID,
    'name': 'Reading graph',
    'unit': 'pages',
    'type': 'int',
    'color': 'sora'
}
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
# response = requests.post(url=graph_endpoint, json=gragh_params, headers=header)
# print(response.text)


# ---------------------------- POST A PIXEL ------------------------------- #
# formated_date = datetime(year=2023, month=8, day=13).strftime("%Y%m%d")
formated_date = datetime.now().strftime("%Y%m%d")
post_pixel_params = {
    'date': formated_date,
    'quantity': input('How many pages have you read today? ')
}
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=header)
print(response.text)


# ---------------------------- UPDATE A PIXEL ------------------------------- #
formated_date = datetime(year=2023, month=8, day=13).strftime("%Y%m%d")
update_pixel_params = {
    'quantity': '12'
}
# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formated_date}"
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=header)
# print(response.text)


# ---------------------------- DELETE A PIXEL ------------------------------- #
# formated_date = datetime(year=2023, month=8, day=13).strftime("%Y%m%d")
# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formated_date}"
# response = requests.delete(url=delete_pixel_endpoint, headers=header)
# print(response.text)