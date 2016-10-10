__author__ = 'Avi Schwartz - Schwartz210@gmail.com'
'''
Project outline:
    PyFy stands for Python Finance. It an application designed for stock market analysis.

Key features:
    Gets stock market data via Yahoo! Finance API.
    Stores in SQL database via sqlite3.
    GUI interface based off tkinter.
    Graphing from Matplotlib
'''

from yahoo_finance import Share
from time import sleep

def pull(ticker, start_date, end_date):
    try:
        stock = Share(ticker)
        return stock.get_historical(start_date, end_date)
    except:
        sleep(1)
        return pull(ticker, start_date, end_date)




data = pull('GOOG','2014-04-25', '2016-04-29')
for record in data:
    print(record)