
# from gpiozero import LED
from gpiozero import PWMLED
from time import sleep
from signal import pause

light = PWMLED(21)
# light = LED(21) # 21 is the pin that the LED in the button is connected to.
# light.blink()
# pause()
# while True:
#     light.value = 0
#     sleep(1)
#     light.value = .5
#     sleep(1)
#     light.value = 1
#     sleep(1)

light.pulse()
pause()