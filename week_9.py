GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')

while GPIO.input(channel) == GPIO.LOW:
    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things

GPIO.wait_for_edge(channel, GPIO.RISING)

channel = GPIO.wait_for_edge(channel, GPIO_RISING, timeout=5000)
if channel is None:
    print('Timeout occurred')
else:
    print('Edge detected on channel', channel)

GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel
do_something()
if GPIO.event_detected(channel):
    print('Button pressed')

def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')

GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)  # add rising edge detection on a channel

def my_callback_one(channel):
    print('Callback one')

def my_callback_two(channel):
    print('Callback two')

GPIO.add_event_detect(channel, GPIO.RISING)
GPIO.add_event_callback(channel, my_callback_one)
GPIO.add_event_callback(channel, my_callback_two)
