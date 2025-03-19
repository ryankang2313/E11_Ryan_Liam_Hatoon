import RPi.GPIO as GPIO
import time
import datetime

# Define GPIO pin for the radiation sensor
SENSOR_PIN = 16  # Change this if using a different pin

# Global variable for counting pulses
pulse_count = 0

# Callback function to count pulses and print timestamp
def count_pulse(channel):
    global pulse_count
    pulse_count += 1
    print(f"▲ Pulse detected at {datetime.datetime.now()}")

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Use pull-down resistor

# Detect falling-edge pulses
GPIO.add_event_detect(SENSOR_PIN, GPIO.FALLING, callback=count_pulse, bouncetime=10)

try:
    while True:
        # Wait for a minute while counting pulses
        time.sleep(60)

        # Print pulse count every minute
        print(f"▼ Counts in last minute: {pulse_count}")

        # Reset count for next minute
        pulse_count = 0

except KeyboardInterrupt:
    print("\nExiting program...")

finally:
    GPIO.cleanup()
    print("GPIO cleanup complete.")
