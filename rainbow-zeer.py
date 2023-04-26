
from gpiozero import Button
import serial
import adafruit_thermal_printer
from gtts import gTTS
import os
from gpiozero import PWMLED
from time import sleep
import random
import textwrap

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000) # Sets up serial connection
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69) # Gets printer class
printer = ThermalPrinter(uart) # Sets up printer
button = Button(27) # Connect the white wire is connected to GPIO27 or Pin 13
light = PWMLED(13) # Connect button LED to GPIO13 or Pin 39
light.value = 1
def playMessage(message = "No Fortune"):
    tts = gTTS(message, lang='en', tld='ie')
    with open('test.mp3', 'wb') as f:
        tts.write_to_fp(f)

    os.system('mplayer test.mp3')

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
    print("turn LED off button")
#    light = PWMLED(21)
    light.off()

def get_fortune():
    fortunes = []
    with open("fortunes.txt", "r") as f:
        fortunes = f.readlines()
    
    fortune = fortunes[random.randint(0, len(fortunes)-1)]
    if(len(fortune) > 16):
        fortune = '\n'.join(textwrap.wrap(fortune, 16))

    return fortune


def swirlyBall():
    print("swirly ball")
    
def solidBall():
    print("solid ball")



while(True):
    button_pulse()
    solidBall()
    print("waiting")
    button.wait_for_press()
    print("pressed")
    button_off()
    swirlyBall()
    fortune = get_fortune()
    playMessage(fortune)
    printMessage(fortune)
    #Wait for print? if not possible, just sleep for a good moment before resetting
    # sleep(1.0)