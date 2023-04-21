import board
import neopixel
import time


LED_COUNT = 16
LED_PIN = board.D18
ORDER = neopixel.GRB

auto_write = False
brightness = 1
brightness_step = .01
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, auto_write=auto_write, pixel_order=ORDER, bpp=4)

def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos*3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r,g,b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(LED_COUNT):
            pixel_index = (i * 256 // LED_COUNT) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    rainbow_cycle(0.001)
