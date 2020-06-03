from tkinter import *
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

## Lights ##
Red = LED(14)
Green = LED(15)
Blue = LED(18)

## Initailse GUI ##
window = Tk()
window.title("Led Toggler")

## Actions ##
def RedLEDToggle():
    Red.on()
    Green.off()
    Blue.off()

def GreenLEDToggle():
    Red.off()
    Green.on()
    Blue.off()

def BlueLEDToggle():
    Red.off()
    Green.off()
    Blue.on()

def close():
    GPIO.cleanup()
    window.destroy()

## Widgets ##
v = IntVar()
RedLedButton = Radiobutton(window, text = "Turn Red LED On", variable=v, value=1, command = RedLEDToggle, height = 2, width = 24)
RedLedButton.grid(row = 0, column = 0)
GreenLedButton = Radiobutton(window, text = "Turn Green LED On", variable=v, value=2, command = GreenLEDToggle, height = 2, width = 24)
GreenLedButton.grid(row = 0, column = 1)
BlueLedButton = Radiobutton(window, text = "Turn Blue LED On", variable=v, value=3, command = BlueLEDToggle, height = 2, width = 24)
BlueLedButton.grid(row = 0, column = 2)

ExitButton = Button(window, text = "Exit", command = close, height = 1, width = 6)
ExitButton.grid(row = 1, column = 3)
window.protocol("WM_DELETE_WINDOW", close)

## Even Handler ##
window.mainloop()


