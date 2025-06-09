
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

# Your Bitcoin prices over the last 10 days
ten_Month = [58000, 635500, 706800, 96200, 93000, 102500, 84300, 82400, 940500, 104200]
tenDay = [108000, 105500, 106800, 103200, 105000, 104500, 104300, 106400, 100500, 105200]
values = np.array(tenDay)

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
plt.title("Bitcoin Price Prediction for Next 5 Days")
plt.legend()
plt.show()

# Print predicted prices
for day, price in zip(future_days.flatten(), predicted_prices):
    print(f"Predicted price on day {day}: ${price:.2f}")




