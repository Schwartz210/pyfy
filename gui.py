__author__ = 'Avi Schwartz - Schwartz210@gmail.com'
from tkinter import *
from db_interface import get_ticker_list, get_date_close
from matplotlib import pyplot
import matplotlib.dates as mdates
from datetime import datetime

class HomeScreen(object):
    def __init__(self):
        self.master = Tk()
        self.option_text = StringVar()
        self.option_text.set('Ticker')
        symbols = get_ticker_list()
        w = OptionMenu(self.master, self.option_text, *symbols)
        w.pack()
        Button(self.master, text='Show Plot', command=self.show_plot).pack()
        self.master.mainloop()

    def show_plot(self):
        symbol = self.option_text.get()
        dates, close_amounts = get_date_close(symbol)
        x = [datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
        y = range(len(x))
        pyplot.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
        pyplot.gca().xaxis.set_major_locator(mdates.DayLocator())
        pyplot.plot(x,y)
        pyplot.gcf().autofmt_xdate()
        pyplot.show()

def run():
    HomeScreen()

