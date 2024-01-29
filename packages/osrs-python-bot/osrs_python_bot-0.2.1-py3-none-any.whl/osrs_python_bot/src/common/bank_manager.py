"""Module providing a function for bank interactions."""
import time
import pyautogui

def withdraw_all(a, b, c):
    """moves the mouse to withdraw all when hovering bank item"""
    x,y = pyautogui.position()
    x_coordinate = x
    y_coordinate = float(y + 100)
    wait_time = float('.2' + b + a + c)
    pyautogui.rightClick()
    pyautogui.moveTo(x_coordinate, y_coordinate, wait_time)
    pyautogui.click()

def deposit_inventory(a, b, c):
    """Clicks Deposit Inventory"""
    x = float('435.'+ b + c)
    y = float('333.'+ b + c)
    wait_time = float('.3'+ b + a + c)
    pyautogui.moveTo(x, y, wait_time)
    pyautogui.click()
    print('depositing inventory')

def close_bank_menu():
    """Closes the bank menu"""
    pyautogui.press('escape')
    print('closing bank menu')

def open_bank_chest(a, b, c):
    """Open bank chest."""
    x_coordinate = float('41' + a + '.'+ b + c)
    y_coordinate = float('12' + a + '.'+ b + c)
    pyautogui.moveTo(x_coordinate, y_coordinate)
    pyautogui.click()
    # wait for chest to open
    wait_time = float('1.'+ b + a + c)
    time.sleep(wait_time)
    print('opening bank chest')

def withdraw_one_1_5(a, b, c):
    """Stub."""
    x_coordinate = float('27' + a + '.'+ b + c)
    y_coordinate = float('11' + a + '.'+ b + c)
    wait_time = float('.2'+ b + a + c)
    pyautogui.moveTo(x_coordinate, y_coordinate, wait_time)
    pyautogui.click()

def withdraw_two_1_6(a, b, c):
    """Stub."""
    x_coordinate = float('32' + a + '.'+ b + c)
    y_coordinate = float('11' + a + '.'+ b + c)
    wait_time = float('.2' + b + a + c)
    pyautogui.moveTo(x_coordinate, y_coordinate, wait_time)
    pyautogui.click()
    pyautogui.click()

def mouse_to_bank_slot_1_7(a, b, c):
    """Stub."""
    x_coordinate = float('37' + a + '.'+ b + c)
    y_coordinate = float('11' + a + '.'+ b + c)
    wait_time = float('.2' + b + a + c)
    pyautogui.moveTo(x_coordinate, y_coordinate, wait_time)

def withdraw_one_1_7(a, b, c):
    """Stub."""
    mouse_to_bank_slot_1_7(a, b, c)
    pyautogui.click()

def mouse_to_bank_slot_1_8(a, b, c):
    """Stub."""
    x_coordinate = float('42' + a + '.'+ b + c)
    y_coordinate = float('11' + a + '.'+ b + c)
    wait_time = float('.2' + b + a + c)
    pyautogui.moveTo(x_coordinate, y_coordinate, wait_time)

def withdraw_one_1_8(a, b, c):
    """Stub."""
    mouse_to_bank_slot_1_8(a, b, c)
    pyautogui.click()
