# Q2.py

import matplotlib.pyplot as plt

# Load data from "sample_AAPL.txt"
with open("sample_AAPL.txt", "r") as f:
    apple_prices = [float(line) for line in f]

# Create x-axis values (Day from 1 to 252)
x_values = range(1, len(apple_prices) + 1)

# Plot the line graph with specified features
plt.plot(x_values, apple_prices)
plt.title('Apple Stock Price, Nov 2019 to Nov 2020')
plt.xlabel('Day')
plt.ylabel('Trading price')
plt.show()
