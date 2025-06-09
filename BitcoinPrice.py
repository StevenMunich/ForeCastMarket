import requests

import datetime


num_days = 10
prices = []
date = datetime.datetime.today()

for i in range(num_days):
    date = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime('%d-%m-%Y')
    #data = .get_coin_history_by_id(id='bitcoin', date=date, localization=False)
    #prices.append((date, data['market_data']['current_price']['usd']))


url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin", "vs_currencies": "usd", "date":date}
response = requests.get(url, params=params)
data = response.json()

print(f"Bitcoin price: ${data}")