import pyautogui as p
from PIL import Image
from threading import Timer
import time
plateindex = [1,1,1,1,1,1]
order = ['', '', '', '', '', '']
ing = {'rice': 10, 'nori': 10, 'roe': 10}
'''
Adding Ingredients
'''

def rice():
    p.click(110,525)
    time.sleep(0.2)
def nori():
    p.click(55,580)
    time.sleep(0.2)
def roe():
    p.click(110,580)
    time.sleep(0.2)

def roller():
    p.click(220,580)
    time.sleep(0.2)

'''
Making Sushi
'''

def makeOnigiri():
    print('Making Onigiri')
    if ing['rice'] >= 2 and ing['nori'] >= 1:
        rice()
        nori()
        rice()
        roller()
        ing['rice'] -= 2
        ing['nori'] -= 1
        try:
            i = order.index('onigiri')
            order[i] = ''
            plateindex[i] = 0
        except ValueError:
            print('?')
        time.sleep(1)
    else:
        print('Not enough ingredients to make Onigiri')

def makeCaliRoll():
    print('Making CaliRoll')
    if ing['rice'] >= 1 and ing['nori'] >= 1 and ing['roe'] >= 1:
        rice()
        nori()
        roe()
        roller()
        ing['rice'] -= 1
        ing['nori'] -= 1
        ing['roe'] -= 1
        try:
            i = order.index('cali')
            order[i] = ''
            plateindex[i] = 0
        except ValueError:
            print('?')
        time.sleep(1)
    else:
        print('Not enough ingredients to make Cali')

def makeGunkan():
    print('Making Gunkan')
    if ing['rice'] >= 1 and ing['nori'] >= 1 and ing['roe'] >= 2:
        roe()
        rice()
        nori()
        roe()
        roller()
        ing['rice'] -= 1
        ing['nori'] -= 1
        ing['roe'] -= 2
        try:
            i = order.index('gunkan')
            order[i] = ''
            plateindex[i] = 0
        except ValueError:
            print('?')
        time.sleep(1)
    else:
        print('Not enough ingredients to make Gunkan')

'''
Ordering Ingredients
'''
def cancelCall():
    p.click(600,525)

def phone():
    p.click(600,550)
def topping():
    p.click(555,465)

def addRice():
    ing['rice'] += 10
    print('10 Rice Added')

def addNori():
    ing['nori'] += 10
    print('10 Nori Added')

def addRoe():
    ing['roe'] += 10
    print('10 Roe Added')

def riceOrder():
    phone()
    p.click(555,485)
    if p.locateOnScreen('rnem.png'):
        print('Not enough money to order Rice')
        cancelCall()
    else:
        p.click(565,470)
        p.click(510,490)
        time.sleep(6)
        addRice()
def noriOrder():
    phone()
    topping()
    if p.locateOnScreen('nnem.png'):
        print('Not enough money to order Nori')
        cancelCall()
    else:
        p.click(515,465)
        p.click(510,490)
        time.sleep(6)
        addNori()

def roeOrder():
    phone()
    topping()
    if p.locateOnScreen('roenem.png'):
        print('Not enough money to order Roe')
        cancelCall()
    else: 
        p.click(595,465)
        p.click(510,490)
        time.sleep(6)
        addRoe()


'''
Clearing Plates
'''

#0 dont make, 1 is make
def clearPlate():
    plates = list(p.locateAllOnScreen('plate.png'))
    for i in plates:
        if i[0] < 70:
            plateindex[0] = 1
        elif i[0] < 170:
            plateindex[1] = 1
        elif i[0] < 270:
            plateindex[2] = 1
        elif i[0] < 370:
            plateindex[3] = 1
        elif i[0] < 470:
            plateindex[4] = 1
        elif i[0] < 570:
            plateindex[5] = 1
    if plates != 0:
        p.click(90,400)
        p.click(190,400)
        p.click(290,400)
        p.click(390,400)
        p.click(490,400)
        p.click(590,400)

'''
Checking Orders
Add to order list, time after x after dish made, remove from order list.
'''

def checkOrder():

    gk = list(p.locateAllOnScreen('gunkan.png'))
    cr = list(p.locateAllOnScreen('caliroll.png'))
    og = list(p.locateAllOnScreen('onigiri.png'))
    for i in gk:
        if i[0] < 70:
            order[0] = 'gunkan'
        elif i[0] < 170:
            order[1] = 'gunkan'
        elif i[0] < 270:
            order[2] = 'gunkan'
        elif i[0] < 370:
            order[3] = 'gunkan'
        elif i[0] < 470:
            order[4] = 'gunkan'
        elif i[0] < 570:
            order[5] = 'gunkan'
    for i in cr:
        if i[0] < 70:
            order[0] = 'cali'
        elif i[0] < 170:
            order[1] = 'cali'
        elif i[0] < 270:
            order[2] = 'cali'
        elif i[0] < 370:
            order[3] = 'cali'
        elif i[0] < 470:
            order[4] = 'cali'
        elif i[0] < 570:
            order[5] = 'cali'
    for i in og:
        if i[0] < 70:
            order[0] = 'onigiri'
        elif i[0] < 170:
            order[1] = 'onigiri'
        elif i[0] < 270:
            order[2] = 'onigiri'
        elif i[0] < 370:
            order[3] = 'onigiri'
        elif i[0] < 470:
            order[4] = 'onigiri'
        elif i[0] < 570:
            order[5] = 'onigiri'

    print(order)

'''
Checking Ingredients, order if low
{'rice', 'nori', 'roe'}
'''

def ingCheck(ing):
    for key, value in ing.items():
        if value <= 3:
            if key == 'rice':
                riceOrder()
            if key == 'nori':
                noriOrder()
            if key == 'roe':
                roeOrder()
    print(ing)

def fulfilOrder():
    for i in order:
        ingCheck(ing)
        if i == 'gunkan':
            makeGunkan()
        elif i == 'onigiri':
            makeOnigiri()
        elif i == 'cali':
            makeCaliRoll()