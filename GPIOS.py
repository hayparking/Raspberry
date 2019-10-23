import RPi.GPIO as gpio

class controller():

    def __init__(self):
        self.state = [False, False, False]
        self.pins = [2, 3, 4]
        gpio.setmode(gpio.BCM)

    def changeState(self, pin, state):
        gpio.setup(self.pins[pin], gpio.OUT)
        gpio.output(self.pins[pin], state)
        self.state[pin] = state
			
    def cleanAll(self):
        for i in range(1, 41):
			gpio.setup(i, gpio.OUT)
			gpio.cleanup(i)
			print("GPIO: "+str(i))
