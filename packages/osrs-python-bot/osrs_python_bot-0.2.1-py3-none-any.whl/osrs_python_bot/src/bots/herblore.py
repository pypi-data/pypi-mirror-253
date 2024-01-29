"""Module for Herblore."""
from random import randrange
import time
import pyautogui
from ..common.bank_manager import withdraw_all
from ..common.bank_manager import mouse_to_bank_slot_1_8
from ..common.bank_manager import deposit_inventory
from ..common.bank_manager import close_bank_menu
from ..common.bank_manager import open_bank_chest
from ..common.inventory_clicker import mouse_to_inventory_slot_1_1
from ..common.inventory_clicker import mouse_to_inventory_slot_1_2
from ..common.inventory_clicker import mouse_to_inventory_slot_1_3
from ..common.inventory_clicker import mouse_to_inventory_slot_1_4
from ..common.inventory_clicker import mouse_to_inventory_slot_2_1
from ..common.inventory_clicker import mouse_to_inventory_slot_2_2
from ..common.inventory_clicker import mouse_to_inventory_slot_2_3
from ..common.inventory_clicker import mouse_to_inventory_slot_2_4
from ..common.inventory_clicker import mouse_to_inventory_slot_3_1
from ..common.inventory_clicker import mouse_to_inventory_slot_3_2
from ..common.inventory_clicker import mouse_to_inventory_slot_3_3
from ..common.inventory_clicker import mouse_to_inventory_slot_3_4
from ..common.inventory_clicker import mouse_to_inventory_slot_4_1
from ..common.inventory_clicker import mouse_to_inventory_slot_4_2
from ..common.inventory_clicker import mouse_to_inventory_slot_4_3
from ..common.inventory_clicker import mouse_to_inventory_slot_4_4
from ..common.inventory_clicker import mouse_to_inventory_slot_5_1
from ..common.inventory_clicker import mouse_to_inventory_slot_5_2
from ..common.inventory_clicker import mouse_to_inventory_slot_5_3
from ..common.inventory_clicker import mouse_to_inventory_slot_5_4
from ..common.inventory_clicker import mouse_to_inventory_slot_6_1
from ..common.inventory_clicker import mouse_to_inventory_slot_6_2
from ..common.inventory_clicker import mouse_to_inventory_slot_6_3
from ..common.inventory_clicker import mouse_to_inventory_slot_6_4
from ..common.inventory_clicker import mouse_to_inventory_slot_7_1
from ..common.inventory_clicker import mouse_to_inventory_slot_7_2
from ..common.inventory_clicker import mouse_to_inventory_slot_7_3
from ..common.inventory_clicker import mouse_to_inventory_slot_7_4
from ..common.bank_manager import withdraw_one_1_5
from ..common.bank_manager import withdraw_two_1_6
from ..common.bank_manager import withdraw_one_1_7
from ..common.bank_manager import withdraw_one_1_8

class Herblore:
    """Herblore bots."""
    def __init__(self):
        """Constructor"""

    def herb_cleaner(self):
        """function for cleaning herbs."""
        max_timeout = time.time() + 30000
        while True:
            if time.time() > max_timeout:
                break

            x = str(randrange(10))              # global random number generation
            y = str(randrange(10))              # global random number generation
            z = str(randrange(10))              # global random number generation


            open_bank_chest(x, y, z)            # open the bank chest
            deposit_inventory(x, y,z)           # deposit inventory
            mouse_to_bank_slot_1_8(x, y, z)
            withdraw_all(x, y, z)

            close_bank_menu()                   # close bank menu

            mouse_to_inventory_slot_1_1(x, y, z)# click every inventory slot
            pyautogui.click()
            mouse_to_inventory_slot_1_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_1_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_1_4(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_2_1(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_2_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_2_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_2_4(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_3_1(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_3_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_3_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_3_4(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_4_1(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_4_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_4_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_4_4(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_5_1(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_5_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_5_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_5_4(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_6_1(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_6_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_6_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_6_4(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_7_1(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_7_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_7_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_7_4(x, y, z)
            pyautogui.click()

            time.sleep(2)


    def guthix_rest_maker(self):
        """function for making guthix rest."""
        max_timeout = time.time() + 30000
        while True:
            if time.time() > max_timeout:
                break

            y = str(randrange(10))                      # global random number generation
            x = str(randrange(10))                      # global random number generation
            z = str(randrange(10))                      # global random number generation

            open_bank_chest(x, y, z)                    # open the bank chest
            deposit_inventory(x, y,z)                   # deposit inventory

            for _ in range(5):                          # loop over six item sets
                a = str(randrange(10))                  # scoped random number generation
                b = str(randrange(10))                  # scoped random number generation
                c = str(randrange(10))                  # scoped random number generation

                withdraw_one_1_5(a, b, c)               # take one cup of hot water
                withdraw_two_1_6(a, b, c)               # take two guam leaf
                withdraw_one_1_7(a, b, c)               # take one marrentill
                withdraw_one_1_8(a, b, c)               # take one harralander

            close_bank_menu()                           # close bank chest

            #########################
            # make 1st guthix reset #
            #########################

            # click 1st guam leaf
            # click cup of water
            mouse_to_inventory_slot_1_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_1_1(x, y, z)
            pyautogui.click()

            # click 2nd guam leaf
            # click cup of water
            mouse_to_inventory_slot_1_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_1_1(y, x, z)
            pyautogui.click()

            # click marrentill
            # click cup of water
            mouse_to_inventory_slot_1_4(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_1_1(y, x, z)
            pyautogui.click()

            # click harralander
            # click cup of water
            mouse_to_inventory_slot_2_1(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_1_1(x, y, z)
            pyautogui.click()

            print('made 1st guthix rest')

            # #########################
            # # make 2nd guthix reset #
            # #########################

            # click 1st guam leaf
            # click cup of water
            mouse_to_inventory_slot_2_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_2_2(x, y, z)
            pyautogui.click()

            # click 2nd guam leaf
            # click cup of water
            mouse_to_inventory_slot_2_4(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_2_2(y, x, z)
            pyautogui.click()

            # click marrentill
            # click cup of water
            mouse_to_inventory_slot_3_1(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_2_2(y, x, z)
            pyautogui.click()

            # click harralander
            # click cup of water
            mouse_to_inventory_slot_3_2(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_2_2(x, y, z)
            pyautogui.click()

            print('made 2nd guthix rest')

            #########################
            # make 3rd guthix reset #
            #########################

            # click 1st guam leaf
            # click cup of water
            mouse_to_inventory_slot_3_4(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_3_3(x, y, z)
            pyautogui.click()

            # click 2nd guam leaf
            # click cup of water
            mouse_to_inventory_slot_4_1(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_3_3(y, x, z)
            pyautogui.click()

            # click marrentill
            # click cup of water
            mouse_to_inventory_slot_4_2(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_3_3(y, x, z)
            pyautogui.click()

            # click harralander
            # click cup of water
            mouse_to_inventory_slot_4_3(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_3_3(x, y, z)
            pyautogui.click()

            print('made 3rd guthix rest')

            #########################
            # make 4th guthix reset #
            #########################

            # click 1st guam leaf
            # click cup of water
            mouse_to_inventory_slot_5_1(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_4_4(x, y, z)
            pyautogui.click()

            # click 2nd guam leaf
            # click cup of water
            mouse_to_inventory_slot_5_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_4_4(y, x, z)
            pyautogui.click()

            # click marrentill
            # click cup of water
            mouse_to_inventory_slot_5_3(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_4_4(y, x, z)
            pyautogui.click()

            # click harralander
            # click cup of water
            mouse_to_inventory_slot_5_4(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_4_4(x, y, z)
            pyautogui.click()

            print('made 4th guthix rest')

            #########################
            # make 5th guthix reset #
            #########################

            # click 1st guam leaf
            # click cup of water
            mouse_to_inventory_slot_6_2(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_6_1(x, y, z)
            pyautogui.click()

            # click 2nd guam leaf
            # click cup of water
            mouse_to_inventory_slot_6_3(x, y, z)
            pyautogui.click()
            mouse_to_inventory_slot_6_1(y, x, z)
            pyautogui.click()

            # click marrentill
            # click cup of water
            mouse_to_inventory_slot_6_4(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_6_1(y, x, z)
            pyautogui.click()

            # click harralander
            # click cup of water
            mouse_to_inventory_slot_7_1(y, z, x)
            pyautogui.click()
            mouse_to_inventory_slot_6_1(x, y, z)
            pyautogui.click()

            print('made 5th guthix rest')
            time.sleep(2.5)
