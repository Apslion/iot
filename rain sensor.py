import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(13, GPIO.IN)

while(True):
    bs = GPIO.input(13)
    if bs == 1:
        GPIO.output(40, GPIO.HIGH)
        print("Rain is detected")
        time.sleep(1)
    else:
        GPIO.output(40, GPIO.LOW)
        print("Rain not detected")
        time.sleep(1)

GPIO.cleanup()