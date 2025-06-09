# Get historical Bitcoin prices for the last 10 days
# Fit into linear regression model
# Plot & View
import time
import numpy as np
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
from sklearn.linear_model import LinearRegression
from pycoingecko import CoinGeckoAPI
import datetime

# Initialize API
cg = CoinGeckoAPI()

#Main Array
prices = []
num_months = 10 # NOT YET

for i in range(num_months):

    date = (datetime.datetime.today() - relativedelta(months=i)).strftime('%d-%m-%Y')
    print(f"Date for month {i + 1}: {date}")
    data = cg.get_coin_history_by_id(id='chainlink', date=date, localization=False)
    print("Retrieved: ", data, " " , date)
    price = data['market_data']['current_price']['usd']
    prices.append(int(price))
    print(price)
    time.sleep(7)
    #End Loop
print(prices)
print("Chainlink Prices for the Last 10 Days:", prices)


#VALUES FROM MAIN VALUES SHOULD BE NEAR
#Old_version_monthlyPrices = [58000, 63000, 70600, 96000, 93000, 102500, 84300, 82400, 94500, 104200]
prices.reverse() #in-order from Last 10 month to Now
print(prices)

values = np.array(prices)
months = np.arange(1, len(values) + 1).reshape(-1, 1)  # X-axis (Days)
#chainlink_prices = [13.21, 13.78, 13.83, 14.01, 13.71, 14.47, 13.90, 13.65, 13.50, 13.40]
#values = chainlink_prices


# Train linear regression model
model = LinearRegression()
model.fit(months, values)
# Predict next 5 days
future_days = np.arange(len(values) + 1, len(values) + 6).reshape(-1, 1)
predicted_prices = model.predict(future_days)

# Plot data
plt.scatter(months, values, color='blue', label="Actual Prices")
plt.plot(months, model.predict(months), color='red', label="Regression Line")
plt.scatter(future_days, predicted_prices, color='green', label="Forecasted Prices")
plt.xlabel("Months")
plt.ylabel("Chainlink Price ($)")
plt.title("Chain link Price Prediction for Next 5 Months")
plt.legend()
plt.show()

# Print predicted prices
for day, price in zip(future_days.flatten(), predicted_prices):
    print(f"Predicted price on month {day}: ${price:.2f}")




