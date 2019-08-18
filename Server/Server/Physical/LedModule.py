from Physical.BaseModule import BaseModule
from gpiozero import LED
from Communication.Message import Message, MessageType
from Communication.EventBus import EventBus

class LedModule(BaseModule):
    def __init__(self, led: LED, event_bus: EventBus):
        self.led = led
        self.event_bus = event_bus

    def power_up(self):
        self.event_bus.register(self, MessageType.LedCommand)

    def power_down(self):
        self.event_bus.unregister(self.get_name())
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


