
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

# This function plays a message, given a string. If the message is in the audio directory,
# then it will play it. Otherwise, it will play the No_Fortune.mp3 file.
# This function takes the fortune message as an argument
def playMessage(message = "No Fortune"):
    # This creates the filename for the mp3 file
    mp3File = f"./audio/{message.replace(' ', '_').replace('\n', '').replace('.', '')}.mp3"
    # Check to see if the file exists
    if os.path.exists(mp3File):
        # If it does, play the file
        os.system(f'mpg321 -q {mp3File}')
        # Return the message
        return message
    else:
        # If the file does not exist, play the No_Fortune.mp3 file
        os.system(f'mpg321 -q ./audio/standard/No_Fortune.mp3')
        # Return a generic message
        return "Your future is unclear to me"

# This function prints a message to the printer. It checks if there is paper in the printer
# and if there is not it plays a message instead. It then prints the message and a random
# number between 0 and 100. It then feeds the printer 5 times to ensure the paper is
# completely ejected. 
def printMessage(message = "No Fortune"):
    if not printer.has_paper:
        os.system(f'mpg321 -q ./audio/standard/No_Paper.mp3')
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
    os.system(f'mpg321 -q ./audio/standard/intro.mp3')
    swirlyBall()
    fortune = get_fortune()
    fortune = playMessage(fortune)
    printMessage(fortune)
