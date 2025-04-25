import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Pin Definitions
LED_PINS = [17, 18, 27, 22]      # GPIO pins for LEDs
SWITCH_PINS = [23, 24, 25, 4]     # GPIO pins for Switches

# Setup GPIO pins
for led_pin in LED_PINS:
    GPIO.setup(led_pin, GPIO.OUT)  # Set LED pins as output

for switch_pin in SWITCH_PINS:
    GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set switch pins as input with pull-down

try:
    while True:
        # Read the state of the switches
        switch_states = [GPIO.input(pin) for pin in SWITCH_PINS]

        # Control LEDs based on switch states
        for i, switch_state in enumerate(switch_states):
            if switch_state == GPIO.HIGH:  # If the corresponding switch is pressed
                GPIO.output(LED_PINS[i], GPIO.HIGH)  # Turn ON the corresponding LED
            else:
                GPIO.output(LED_PINS[i], GPIO.LOW)   # Turn OFF the corresponding LED

        time.sleep(0.1)  # Small delay to debounce switches

except KeyboardInterrupt:
    print("Program stopped")

finally:
    GPIO.cleanup()  # Clean up GPIO settings before exiting