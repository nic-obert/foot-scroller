import serial
from pynput.mouse import Controller, Button

port = serial.Serial('/dev/ttyACM0')

mouse = Controller()

while True:
    inp = port.read()
    if 0 == int(inp):
        print('scroll down')
        mouse.scroll(0, 2)
    else:
        print('scroll up')
        mouse.scroll(0, -2)



