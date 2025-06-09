import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
values = [115000, 113500, 111800, 110200, 109000, 107500, 106300, 105000, 104500, 103200]
#values = [108000, 105500, 106800, 103200, 105000, 104500, 104300, 1064000, 100500, 105200]
# Simulated Bitcoin price data (downward trend)
days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
prices = np.array(values)  # Prices decreasing

# Create and fit the linear regression model
model = LinearRegression()
model.fit(days, prices)

# Predict future prices (next 5 days)
future_days = np.array([11, 12, 13, 14, 15]).reshape(-1, 1)
predicted_prices = model.predict(future_days)

# Plot actual data
plt.scatter(days, prices, color='blue', label="Actual Prices")
plt.plot(days, model.predict(days), color='red', label="Regression Line")
plt.scatter(future_days, predicted_prices, color='green', label="Forecasted Prices")
plt.xlabel("Days")
plt.ylabel("Bitcoin Price ($)")
plt.title("Bitcoin Price Decline Forecast")
plt.legend()
plt.show()

# Print predicted future prices
for day, price in zip(future_days.flatten(), predicted_prices):
    print(f"Predicted price on day {day}: ${price:.2f}")