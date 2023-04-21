import board
import neopixel
from random import *
from time import sleep
from signal import pause

LED_COUNT = 16
LED_PIN = board.D18
auto_write = False
brightness = 1
brightness_step = .01
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, auto_write=auto_write, bpp=4)

brightness_increasing = False
pixels.fill((255,0,0))
while True:
    if brightness_increasing:
        brightness += brightness_step
        if brightness == 1:
            brightness_increasing = False
    else:
        brightness -= brightness_step
        if brightness <= .1:
            brightness_increasing = True

    pixels.brightness = brightness
    pixels.show()
    sleep(.01)
