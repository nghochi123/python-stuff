import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

testpin = 40

GPIO.setup(testpin, GPIO.IN)

while True:
    print(GPIO.input(testpin))
    time.sleep(0.2)
