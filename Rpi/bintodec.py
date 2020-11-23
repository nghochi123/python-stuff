'''
5 bit Binary calculator
'''

import RPi.GPIO as g
import time
import math

g.setmode(g.BOARD)

pins = [12, 16, 18, 22, 36]

for pin in pins:
    g.setup(pin, g.OUT)

amount = int(input('Please enter a number between 0 and 31: '))
res = []
for i in range(5):
    res.append(amount%2)
    amount = math.floor(amount/2)

res = res[::-1]

print(res)
for i in range(5):
    if(res[i] == 1):
        g.output(pins[i],g.HIGH)
    else:
        g.output(pins[i],g.LOW)
time.sleep(5)
for pin in pins:
    g.output(pin, g.LOW)
