import RPi.GPIO as GPIO
import time

LDR_PIN = 17  # Connect midpoint of voltage divider here

GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)

print("Detecting light...")

try:
    while True:
        if GPIO.input(LDR_PIN) == GPIO.HIGH:
            print("💡 Bright Light Detected!")
        else:
            print("🌑 It's Dark or Dim")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program stopped.")