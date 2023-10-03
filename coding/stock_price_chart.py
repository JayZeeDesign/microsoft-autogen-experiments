# filename: stock_price_chart.py

import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# Define the stocks to download. We would download NVDA, AAPL, and TESLA
ticker_list = ['NVDA', 'AAPL', 'TSLA']

# We would like all available data from 01/01/2022 until today (represents YTD).
start_date = datetime.date(datetime.datetime.now().year, 1, 1)
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

# Use yfinance to load the Yahoo Finance data directly into a pandas DataFrame
stocks_data = yf.download(ticker_list, start=start_date, end=end_date)

# Plot the adjusted close price over time
stocks_data['Adj Close'].plot(figsize=(10,5))
plt.title('Adjusted Close Price (YTD)', fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()