"""Module providing a function for prayer flicking."""
from random import randrange
import time
import pyautogui

class Combat: # pylint: disable=too-few-public-methods
    """Combat Bots"""
    def __init__(self):
        """Constructor"""

    def nightmare_zone(self):
        """function nightmare zone prayer flicking."""
        max_timeout = time.time() + 30000
        while True:
            if time.time() > max_timeout:
                break

            a = str(randrange(10)) # random number generation
            b = str(randrange(10)) # random number generation
            c = str(randrange(10)) # random number generation
            d = str(randrange(10)) # random number generation

            # random ~30s string -> float
            wait_time = float('30.' + a + b + c + d)
            print( 'Time: '+ str(wait_time))

            # double click
            pyautogui.click()
            pyautogui.click()

            # sleep
            time.sleep(wait_time)
