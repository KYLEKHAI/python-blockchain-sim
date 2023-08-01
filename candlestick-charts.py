#Importing modules

#Data visualizer
import matplotlib.pyplot as plt 

#Access financial data from the web/API
import yfinance as yf

#Library to visualize financial and candlestick charts
import mplfinance as mpf

#Work with dates and times 
import datetime as dt

def get_valid_date(date_str):
    try:
        date = dt.datetime.strptime(date_str, "%Y-%m-%d")
        return date
    
    except ValueError:
        print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
        return None

def get_valid_symbol():
    while True:
        symbol = input("Enter the crypto/stock symbol (e.g., BTC-CAD or AAPL): ").upper()

        #Check at least 3 year worth of data for requested symbol
        data = yf.download(symbol, start=dt.datetime(2020, 1, 1), end=dt.datetime.now())

        if data.empty:
            print("Invalid symbol. Please enter a valid crypto/stock symbol.")
        else:
            return symbol

#Prompt user to input crypto/stock symbol
symbol = get_valid_symbol()

#Prompt user to input start date
while True:
    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    start_date = get_valid_date(start_date_str)
    if start_date:
        break

#Use current date as end date
end_date = dt.datetime.now()

#Download financial data from Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

#Customize the market colors
colors = mpf.make_marketcolors(up="#00ff00", down="#ff0000", wick="inherit", edge="inherit", volume="in")

#Create a style object with the custom market colors
mpf_style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)

#Plot the candlestick chart with the custom style (ignore too much data warning)
mpf.plot(data, type="candle", style=mpf_style, volume=True,warn_too_much_data=len(data) + 1)