import requests
import ghasedakpack


STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = ''                             #Enter your own api key
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'interval': '5min',
    'apikey': stock_api_key
}
stock_response = requests.get(url = STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

data_list = [value for (key, value) in stock_response.json()['Time Series (Daily)'].items()]
day_before_yesterday_close_price =  float(data_list[0]['4. close'])
yesterday_close_price =  float(data_list[1]['4. close'])
difference = abs(day_before_yesterday_close_price - yesterday_close_price)
the_difference = (difference / yesterday_close_price) * 100


if the_difference > 5:
    news_api_key = ''                         #Enter your own api key
    news_parameters = {
        'q': 'tesla',
        'from': '2023-07-13',
        'sortBy': 'publishedAt',
        'apikey': news_api_key
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()

    the_news = []
    for i in range(3):
        news_title = news_response.json()['articles'][i]['title']
        news_description = news_response.json()['articles'][i]['description']
        the_news.append({news_title: news_description})

    sms = ghasedakpack.Ghasedak('')         #Enter your own api key
    message = f'{news_title}\n{news_description}'
    receptor = ''                           #Enter your own phone number
    linenumber = ''                         #Enter your own linenumber

    sms.send({ 
        'message': message,  
        'receptor' : receptor, 
        'linenumber': linenumber 
        })