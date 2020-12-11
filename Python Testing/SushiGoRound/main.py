import functions as f
import pyautogui
pyautogui.FAILSAFE = True

while True:
    #Check for orders if order empty
    while f.order == ['', '', '', '' ,'' ,'']:
        f.checkOrder()
        f.clearPlate()
    #If order not empty, make order
    f.fulfilOrder()
    f.clearPlate()
    #