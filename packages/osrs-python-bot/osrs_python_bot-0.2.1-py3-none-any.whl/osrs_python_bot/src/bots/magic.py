"""Module providing a function for high alchemy."""
from random import randrange
import time
import pyautogui

class Magic: # pylint: disable=too-few-public-methods
    """Magic bots"""
    def __init__(self):
        """Constructor"""

    def high_alchemy(self):
        """High alchemy function"""
        max_timeout = time.time() + 30000
        while True:
            if time.time() > max_timeout:
                break
            a = randrange(10)
            b = randrange(10)
            c = randrange(10)
            d = randrange(10)
            e = randrange(10)
            wait_time = float('.' + str(a) + str(b) + str(c) + str(d) + str(e))
            print( 'Time: '+ str(wait_time))
            pyautogui.click()
            time.sleep(wait_time)
