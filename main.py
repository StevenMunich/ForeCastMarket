import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#this is our data
daysData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
futureOutputs = [11, 12, 13, 14, 15]
#AI-BSvalues = [105000, 106500, 107800, 109200, 110000, 111500, 112300, 113000, 113500, 114200]
monthlyPrices = [58000, 63000, 70600, 96000, 93000, 102500, 84300, 82400, 94500, 104200]
workingSample = [100000, 105500, 106800, 103200, 105000, 104500, 104300, 1064000, 100500, 105200] #breaks program
values = monthlyPrices
#PROGRAM. Linear Regression Chart for Bitcoin.

# Sample Bitcoin price data (replace with actual values)
days = np.array(daysData).reshape(-1, 1)  # days configure
prices = np.array(values)  #  values configure

# Create and train the linear regression model
model = LinearRegression()
model.fit(days, prices)

# Predict future prices ()
future_days = np.array(futureOutputs).reshape(-1, 1) #futureOutputs Configure
predicted_prices = model.predict(future_days)

# Plot the trend
plt.scatter(days, prices, color='blue', label="Actual Prices")
plt.plot(days, model.predict(days), color='red', label="Regression Line")
plt.scatter(future_days, predicted_prices, color='green', label="Forecasted Prices")
plt.xlabel("Days") #change to Months or days, either or.
plt.ylabel("Bitcoin Price ($)")
plt.title("Bitcoin Price Trend Forecast")
plt.legend()
plt.show()

# Print predicted future prices
#for day, price in zip(future_days.flatten(), predicted_prices):
  #  print(f"Predicted price on day {day}: ${price:.2f}")