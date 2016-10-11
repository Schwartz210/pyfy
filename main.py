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
from db_interface import execute_multiple_sql, add_record

TIME_PERIOD = ('2014-04-25', '2016-04-25')

def pull(ticker):
    start_date, end_date = TIME_PERIOD
    try:
        stock = Share(ticker)
        return stock.get_historical(start_date, end_date)
    except:
        sleep(1)
        return pull(ticker)


def load_into_database(ticker):
    data = pull(ticker)
    sql_requests = []
    for record in data:
        sql_request = add_record(record)
        sql_requests.append(sql_request)
    execute_multiple_sql(sql_requests)

