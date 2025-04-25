import RPi.GPIO as GPIO
import time

# Setup GPIO pins
IR_PIN = 17  # IR sensor output pin connected to GPIO 17
BUZZER_PIN = 18  # Buzzer pin connected to GPIO 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)  # Input for IR sensor
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Output for buzzer

print("IR Sensor and Buzzer Program Running...")

try:
    while True:
        if GPIO.input(IR_PIN) == GPIO.HIGH:  # Object detected
            print("Object detected! Activating buzzer...")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on buzzer
        else:
            print("No object detected.")
            GPIO.output(BUZZER_PIN, GPIO.LOW)  # Turn off buzzer
        time.sleep(0.1)  # Delay to prevent excessive printing

except KeyboardInterrupt:
    GPIO.cleanup()  # Cleanup GPIO on exit
    print("Program stopped.")