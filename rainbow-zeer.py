
from gpiozero import Button
import serial
import adafruit_thermal_printer
from gtts import gTTS
import os
from gpiozero import PWMLED
from time import sleep
import random
import textwrap
import board
import neopixel
import threading

# Printer Config
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000) # Sets up serial connection
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69) # Gets printer class
printer = ThermalPrinter(uart) # Sets up printer

# Button Config
button = Button(27) # Connect the white wire is connected to GPIO27 or Pin 13
light = PWMLED(13) # Connect button LED to GPIO13 or Pin 39
light.value = 1

# NeoPixel Config
LED_COUNT = 16
LED_PIN = board.D21
ORDER = neopixel.GRB

auto_write = False
brightness = 1
brightness_step = .01
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, auto_write=auto_write, pixel_order=ORDER, bpp=4)

def playMessage(message = "No Fortune"):
    tts = gTTS(message, lang='en', tld='ie')
    with open('fortune.mp3', 'wb') as f:
        tts.write_to_fp(f)

    os.system('mplayer fortune.mp3')

def printMessage(message = "No Fortune"):
    if not printer.has_paper:
        playMessage("Oops! I am out of paper, or am disconnected from the printer.")
    else:
        printer._set_size(1)
        print(f"Printing: {message}")
        printer.print('--------------------------------')
        header = 'The Rainbow Zeer has looked into the future and determined:'
        printer.print('\n'.join(textwrap.wrap(header, 32)))
        printer.feed(1)
        printer._set_size(2)
        printer.print(message)
        luckynum = random.randint(0,100)
        printer._set_size(1)
        printer.print(f'Your lucky number is: {luckynum}')
        printer.feed(5)

def button_pulse():
    print('button pulse')
    light.pulse()

def button_off():
    print("turn LED button off")
    light.off()

def get_fortune():
    fortunes = []
    with open("fortunes.txt", "r") as f:
        fortunes = f.readlines()
    
    fortune = fortunes[random.randint(0, len(fortunes)-1)]
    if(len(fortune) > 16):
        fortune = '\n'.join(textwrap.wrap(fortune, 16))

    return fortune

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

def rainbow_cycle():
    while True:
        if event.is_set():
            break
        for j in range(255):
            for i in range(LED_COUNT):
                pixel_index = (i * 256 // LED_COUNT) + j
                pixels[i] = wheel(pixel_index & 255)
            pixels.brightness = 1
            pixels.show()
            sleep(0.001)

def solid_ball():
    pixels.fill((255,255,255))
    pixels.brightness = .3
    pixels.show()

while(True):
    solid_ball()
    button_pulse()
    print("waiting")
    button.wait_for_press()
    print("pressed")
    button_off()
    event = threading.Event()
    swirl_thread = threading.Thread(target=rainbow_cycle, name='swirl')
    swirl_thread.start()
    os.system('mplayer intro.mp3')
    fortune = get_fortune()
    playMessage(fortune)
    
    event.set()
    sleep(1)
    printMessage(fortune)
