from gpiozero import Button
from signal import pause

def press():
    print("You pressed the button")

def release():
    print("You released the button")


button = Button(27) # Connect the white wire is connected to GPIO27 or Pin 13

button.when_pressed = press
button.when_released = release

pause()