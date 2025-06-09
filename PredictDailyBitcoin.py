import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from pycoingecko import CoinGeckoAPI
import datetime

# Initialize API
cg = CoinGeckoAPI()

# Get historical Bitcoin prices for the last 10 days
num_days = 10

#num_months = 10 # NOT YET
#for i in range(num_months):
    # Calculate the date by subtracting i months
    #date = (datetime.today() - relativedelta(months=i)).strftime('%d-%m-%Y')
    #print(f"Date for month {i + 1}: {date}")

#Main Array
prices = []

for i in range(0, 10):

    date = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime('%d-%m-%Y')

    data = cg.get_coin_history_by_id(id='bitcoin', date=date, localization=False)
    #prices.append((date, data['market_data']['current_price']['usd']))
    print("Retrieved: ", data, " " , date)
    price = data['market_data']['current_price']['usd']
    prices.append(int(price))
    print(price)
    time.sleep(10)
    #End Loop
print(prices)
print("Bitcoin Prices for the Last 10 Days:", prices)






values = np.array(prices)

days = np.arange(1, len(values) + 1).reshape(-1, 1)  # X-axis (Days)
#chainlink_prices = [13.21, 13.78, 13.83, 14.01, 13.71, 14.47, 13.90, 13.65, 13.50, 13.40]
#values = chainlink_prices


# Train linear regression model
model = LinearRegression()
model.fit(days, values)

# Predict next 5 days
future_days = np.arange(len(values) + 1, len(values) + 6).reshape(-1, 1)
predicted_prices = model.predict(future_days)

# Plot data
plt.scatter(days, values, color='blue', label="Actual Prices")
plt.plot(days, model.predict(days), color='red', label="Regression Line")
plt.scatter(future_days, predicted_prices, color='green', label="Forecasted Prices")
plt.xlabel("Days")
plt.ylabel("Bitcoin Price ($)")
plt.title("Bitcoin Price Prediction for Next 5 Days/Months")
plt.legend()
plt.show()

# Print predicted prices
for day, price in zip(future_days.flatten(), predicted_prices):
    print(f"Predicted price on day {day}: ${price:.2f}")




