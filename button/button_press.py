from gpiozero import Button
from signal import pause

def press():
    print("You pressed the button")

def release():
    print("You released the button")


button = Button(27) # This is the pin that the white wire is connected to.

button.when_pressed = press
button.when_released = release

pause()