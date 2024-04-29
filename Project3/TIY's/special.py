# Walmart stock from 2020 - 2024 using yfinance

import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol
ticker_symbol = "WMT"

# Download historical data as a Pandas DataFrame
walmart_data = yf.download(ticker_symbol, start="2020-01-01", end="2024-04-28")

# Plot the closing prices
plt.figure(figsize=(10, 6))
plt.plot(walmart_data['Close'], label='Close Price')
plt.title('Walmart Stock Price (2020 - 2024)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()


