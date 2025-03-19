import RPi.GPIO as GPIO
import time
import datetime

GPIO_PIN = 16  # GPIO pin connected to the sensor
BOUNCE_TIME = 200  # Debounce time in milliseconds

# Global variable to store count
pulse_count = 0

# Callback function to handle pulse detection
def pulse_callback(channel):
    global pulse_count
    pulse_count += 1
    print("Pulse detected at", datetime.datetime.now())

try:
    # GPIO setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Falling-edge detection with debounce
    GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=pulse_callback, bouncetime=BOUNCE_TIME)

    print("Waiting for pulses on GPIO pin {}...".format(GPIO_PIN))

    # Infinite loop to print count every minute
    while True:
        time.sleep(60)  # Wait for one minute
        print("Counts in the last minute:", pulse_count)
        pulse_count = 0  # Reset the count after printing

except KeyboardInterrupt:
    print("\nExiting program...")

finally:
    GPIO.cleanup()
    print("GPIO cleanup complete.")
