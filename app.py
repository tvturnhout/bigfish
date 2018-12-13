import datetime
from time import sleep

from automagica import *

import win32api
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
Parameters
"""

# Path to your Chrome user data, can be found by
PATH_TO_USER_DATA = r'C:/Users/USERNAME/AppData/Local/Google/Chrome/User Data'

# Times you want the game to warp in time and gather coins
PREFERRED_AMOUNT_OF_WARPS = 10


def start_big_fish():

    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=" + PATH_TO_USER_DATA)
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chrome_options=chrome_options)

    sleep(3)
    browser.get('https://www.messenger.com/t/bigfishgame?game=big-fish-game')
    sleep(5)
    ClickOnPosition(767, 795)
    sleep(3)
    browser.quit()
    return

def set_historical_date():
    tt = datetime.datetime(2003,8,1,12,4,5)
    win32api.SetSystemTime(tt.year, tt.month, 0, tt.day, tt.hour, tt.minute, tt.second, tt.microsecond//1000)
    return tt

 
def increase_date(current_date):
    tt = current_date + datetime.timedelta(days=2)
    win32api.SetSystemTime(tt.year, tt.month, 0, tt.day, tt.hour, tt.minute, tt.second, tt.microsecond//1000)
    return tt

date = set_historical_date()
for i in range(0,PREFERRED_AMOUNT_OF_WARPS):
    start_big_fish()
    date = increase_date(date)
