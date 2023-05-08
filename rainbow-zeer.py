
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

localpath = "/home/admin/repos/Rainbow-Zeer"

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


# This function plays a message, given a string. If the message is in the audio directory,
# then it will play it. Otherwise, it will play the No_Fortune.mp3 file.
# This function takes the fortune message as an argument
def playMessage(message = "No Fortune"):
    # This creates the filename for the mp3 file
    m = message.replace(' ', '_').replace('\n', '').replace('.', '')
    mp3File = f"{localpath}/audio/{m}.mp3"
    # Check to see if the file exists
    if os.path.exists(mp3File):
        # If it does, play the file
        os.system(f'mpg321 -q {mp3File}')
        # Return the message
        return message
    else:
        # If the file does not exist, play the No_Fortune.mp3 file
        os.system(f'mpg321 -q {localpath}/audio/standard/No_Fortune.mp3')
        # Return a generic message
        return "Your future is unclear to me"

# This function prints a message to the printer. It checks if there is paper in the printer
# and if there is not it plays a message instead. It then prints the message and a random
# number between 0 and 100. It then feeds the printer 5 times to ensure the paper is
# completely ejected. 
def printMessage(message = "No Fortune"):
    if not printer.has_paper:
        os.system(f'mpg321 -q {localpath}/audio/standard/No_Paper.mp3')
    else:
        if(len(fortune) > 16):
            message = '\n'.join(textwrap.wrap(message, 16))
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
    print("turn LED off button")
    light.off()

def get_fortune():
    fortunes = []
    with open(f"{localpath}/fortunes.txt", "r") as f:
        fortunes = f.readlines()
    
    fortune = fortunes[random.randint(0, len(fortunes)-1)]

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
    button_pulse()
    solid_ball()
    print("waiting")
    button.wait_for_press()
    print("pressed")
    button_off()
    event = threading.Event()
    swirl_thread = threading.Thread(target=rainbow_cycle, name='swirl')
    swirl_thread.start()
    os.system(f'mpg321 -q {localpath}/audio/standard/intro.mp3')
    sleep(4)
    fortune = get_fortune()
    print(fortune)
    fortune = playMessage(fortune)
    printMessage(fortune)
    event.set()
    sleep(1)
    
