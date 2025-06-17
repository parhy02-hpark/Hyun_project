'''
You will be given a list of daily stock prices, and you will be asked to 
return the three stocks with the highest price.
Implement the function get_top_stocks(stocks, prices) which takes as input:
  a list of strings (stocks), representing the considered stocks.
  a list of 2 dimensions (prices), representing the stock prices (inner list)
  for each day (outer list).
Your get_top_stocks function should return a list containing the names of the
three stocks with the highest average value. The list should be stored by 
decreasing average value. You're guaranteed that each stock will have a 
unique average value. 
use import sys, math, from contextlib import redirect_stdout
'''
import sys
import math
from contextlib import redirect_stdout
from collections import defaultdict

def get_top_stocks(stocks, prices):
    """return the three stocks with the highest average price."""
    stock_data = defaultdict(list)
    print(stock_data)

    # Collect stock prices from each day
    for daily_prices in prices:
        print("daily_prices: ", daily_prices)
        for stock, price in zip(stocks, daily_prices):
            print("stock: ", stock, " price: ", price)
            stock_data[stock].append(price)
    print(stock_data)
    # Compute average price for each stock
    avg_prices = {stock: sum(prices) / len(prices) for stock, prices in stock_data.items()}
    #print(avg_prices)

    # Sort stocks by decreasing average price and take the top three
    top_stocks_test = sorted(avg_prices.keys(), key=lambda stock: avg_prices[stock], reverse=True)
    print("top stocks test: ", top_stocks_test)
    top_stocks = sorted(avg_prices.keys(), key=lambda stock: avg_prices[stock], reverse=True)[:3]
  
    return top_stocks

stocks = ["AAPL", "GOOGL", "PLTR", "TSLA"]
prices = [
    [150, 148, 90, 349],    # day 1
    [151, 162, 100, 358],    # day 2
    [144, 159, 120, 359],    # day 3
    [154, 164, 130, 370]     # day 4
]

with redirect_stdout(sys.stdout):    # redirecting standard output
    print(get_top_stocks(stocks, prices))
