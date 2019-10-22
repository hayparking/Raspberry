import RPi.GPIO as gpio

class controller():

    pins
    states

    def __init__(self):
        self.state = [False, False, False]
        self.pins = [2, 3, 4]
        gpio.setmode(gpio.BCM)


    def changeState(pin, state):
        gpio.setup(pins[pin], gpio.OUT)
        gpio.output(pins[pin], state)

    def cleanAll():
        GPIO.cleanup()
