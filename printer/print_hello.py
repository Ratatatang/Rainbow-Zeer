import serial
import adafruit_thermal_printer

brate = 19200

uart = serial.Serial("/dev/serial0", baudrate=brate, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

printer = ThermalPrinter(uart)


PrintMe = "Matt is a hacker man!"
printer.print(PrintMe)
printer.feed(2)
