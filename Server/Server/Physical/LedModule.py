from .BaseModule import BaseModule
from gpiozero import LED

class LedModule(BaseModule):
    def __init__(self, pin):
        self.led = LED(pin)

    def get_name(self):
        return "LedModule"

    def process(self, message):
        print(f'Led module recieved a message {message["Payload"]}')

    def on(self):
        self.led.on()
      
    def off(self):
        self.led.off()

    def blink(self):
        self.led.blink(0.5, 0.25);


