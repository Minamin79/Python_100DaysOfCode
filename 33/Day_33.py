import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = '@gmail.com'                 #Enter your own gmail
MY_PASS = ''                            #Enter your own password
MY_LAT = 0.0                            #Enter your own latitude
MY_LONG = 0.0                           #Enter your own longitude


def is_iss_overhead():
    iss_responce =  requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_responce.raise_for_status() 
    iss_lat = float(iss_responce.json()['iss_position']['latitude'])
    iss_long = float(iss_responce.json()['iss_position']['longitude'])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True
    
    
def is_night():
    parameters = {
        'lat':MY_LAT,
        'lng':MY_LONG,
        'formatted':0
        }
    
    sun_response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    sun_response.raise_for_status()
    data = sun_response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject:Look at the sky ^-^\n\nThe ISS is above you in the sky.'
    )