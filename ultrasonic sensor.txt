import RPi.GPIO as GPIO
import time

# Define GPIO pins
TRIG = 23
ECHO = 24

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Measuring distance...")

try:
    while True:
        # Send 10µs pulse to TRIG
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Wait for ECHO to go HIGH
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        # Wait for ECHO to go LOW
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        # Calculate pulse duration
        pulse_duration = pulse_end - pulse_start

        # Calculate distance (speed of sound = 34300 cm/s)
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print("Distance:", distance, "cm")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program stopped.")