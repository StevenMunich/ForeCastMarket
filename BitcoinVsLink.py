import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

# Define crypto list
cryptos = ['bitcoin', 'chainlink']

import time
import requests
from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta

cg = CoinGeckoAPI()


# Function to get historical prices with timeout & retries
def get_historical_prices(crypto, days=10):
    prices = []
    for i in range(days, 0, -1):
        date = (datetime.today() - timedelta(days=i)).strftime('%d-%m-%Y')

        try:
            response = cg.get_coin_history_by_id(id=crypto, date=date)
            prices.append(response['market_data']['current_price']['usd'])
            time.sleep(1)  # Add delay to avoid rate limits
        except requests.exceptions.Timeout:
            print(f"Timeout error for {crypto} on {date}. Skipping...")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {crypto} data: {e}")
            time.sleep(5)  # Wait before retrying

    return prices


# Example usage
crypto_data = get_historical_prices("bitcoin")
print(crypto_data)

# Fetch data for each crypto
crypto_data = {crypto: get_historical_prices(crypto) for crypto in cryptos}

# Create Pandas DataFrame
df = pd.DataFrame(crypto_data)
df.index = np.arange(1, len(df) + 1)
print(df)


# Apply Linear Regression for forecasting
def forecast_prices(prices):
    days = np.arange(1, len(prices) + 1).reshape(-1, 1)
    model = LinearRegression()
    model.fit(days, prices)

    future_days = np.arange(len(prices) + 1, len(prices) + 6).reshape(-1, 1)
    predicted_prices = model.predict(future_days)

    return future_days.flatten(), predicted_prices


# Plot data for each crypto
plt.figure(figsize=(10, 5))

for crypto, prices in crypto_data.items():
    future_days, predicted_prices = forecast_prices(prices)

    plt.scatter(range(1, len(prices) + 1), prices, label=f"Actual {crypto} prices")
    plt.plot(range(1, len(prices) + 1), prices, linestyle='dashed')
    plt.scatter(future_days, predicted_prices, label=f"Forecasted {crypto} prices", marker='x')

plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.title("Crypto Price Forecast (Bitcoin & ChainLink)")
plt.legend()
plt.show()

# Print forecasted prices
for crypto, prices in crypto_data.items():
    future_days, predicted_prices = forecast_prices(prices)
    print(f"\nPredicted prices for {crypto}:")
    for day, price in zip(future_days, predicted_prices):
        print(f"Day {day}: ${price:.2f}")