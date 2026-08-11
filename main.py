import time
from machine import Pin

blue = Pin(2, Pin.OUT)
red = Pin(4, Pin.OUT)
green = Pin(3, Pin.OUT)

while True:
    blue.value(1)
    time.sleep(0.5)
    blue.value(0)
    time.sleep(0.5)

    red.value(1)
    time.sleep(0.5)
    red.value(0)
    time.sleep(0.5)

    green.value(1)
    time.sleep(0.5)
    green.value(0)
    time.sleep(0.5)
