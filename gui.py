__author__ = 'Avi Schwartz - Schwartz210@gmail.com'
from tkinter import *

class HomeScreen(object):
    def __init__(self):
        self.master = Tk()
        option_text = StringVar()
        option_text.set('Ticker')
        things = ["one", "two", "three"]
        w = OptionMenu(self.master, option_text, *things)
        w.pack()
        self.master.mainloop()



def run():
    HomeScreen()

