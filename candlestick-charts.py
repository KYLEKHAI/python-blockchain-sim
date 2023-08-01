#Importing modules

#Data visualizer
import matplotlib.pyplot as plt 

#Access financial data from the web/API
import yfinance as yf

#Library to visualize financial and candlestick charts
import mplfinance as mpf

#Work with dates and times 
import datetime as dt

start = dt.datetime(2015,1,1)
end = dt.datetime.now()

data = yf.download("BTC-CAD", start=start, end=end)

#Customize the market colors
colors = mpf.make_marketcolors(up="#00ff00", down="#ff0000", wick="inherit", edge="inherit", volume="in")

#Create a style object with the custom market colors
mpf_style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)

#Plot the candlestick chart with the custom style
mpf.plot(data, type="candle", style=mpf_style, volume = True)