import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

ledPin = 12

GPIO.setup(ledPin, GPIO.OUT)

for i in range(5):
    print("LED Turning On")
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(0.5)

    print("LED Turning Off")
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(0.5)
