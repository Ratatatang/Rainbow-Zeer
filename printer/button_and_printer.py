from gpiozero import Button
from signal import pause
import serial
import adafruit_thermal_printer

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000) # Sets up serial connection
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69) # Gets printer class
printer = ThermalPrinter(uart) # Sets up printer


button = Button(27) # This is the pin that the white wire is connected to.
print("waiting")
button.wait_for_press()

PrintMe = "Stop pushing my buttons man!"
printer.print(PrintMe)
printer.feed(2)

