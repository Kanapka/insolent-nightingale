from Physical.BaseModule import BaseModule
from gpiozero import LED
from Communication.Message import Message, MessageType
from Communication.EventBus import EventBus

class LedModule(BaseModule):
    def __init__(self, led: LED):
        self.led = led

    def power_up(self):
        super().power_up()
        EventBus().register(self, MessageType.LedCommand)

    def power_down(self):
        super().power_down()
        self.led.close()

    def get_name(self):
        return "LedModule"

    def process(self, message: Message):
        print(f'Led module recieved a message {message.payload}')
        if message.payload == 'On':
            self.on()
        elif message.payload == 'Blink':
            self.blink()
        else:
            self.off()

    def on(self):
        self.led.on()
      
    def off(self):
        self.led.off()

    def blink(self):
        self.led.blink(0.5, 0.25)


