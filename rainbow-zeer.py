from gpiozero import Button
from signal import pause
import serial
import adafruit_thermal_printer
from gtts import gTTS
import os
from gpiozero import PWMLED
from time import sleep

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000) # Sets up serial connection
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69) # Gets printer class
printer = ThermalPrinter(uart) # Sets up printer

def playMessage(message = "No Fortune"):
    tts = gTTS(text, lang='en', tld='ie')
    with open('test.mp3', 'wb') as f:
        tts.write_to_fp(f)

    os.system('mplayer test.mp3')

def printMessage(message = "No Fortune"):
    printer.print(message)
    printer.feed(2)

def blinkLight():
    light = PWMLED(21)
    light.pulse()
    pause()

def solidLight():
    light = PWMLED(21)

button = Button(27) # This is the pin that the white wire is connected to.

while(True):
    blinkLight()
    print("waiting")
    button.wait_for_press()
    print("pressed")
    playMessage()
    printMessage()
    sleep(1.0)