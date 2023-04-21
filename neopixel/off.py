import board
import neopixel
import time


LED_COUNT = 16
LED_PIN = board.D18
ORDER = neopixel.GRB

auto_write = True

pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, auto_write=auto_write, pixel_order=ORDER, bpp=4)

pixels.fill((0,0,0))
pixels.brightness = 0