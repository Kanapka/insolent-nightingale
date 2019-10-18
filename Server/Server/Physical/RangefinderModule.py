from Physical.BaseModule import BaseModule
from Communication.Message import Message, MessageType
from Communication.EventBus import EventBus
from gpiozero import DistanceSensor

class RangefinderModule(BaseModule):
    def __init__(self, rangefinder: DistanceSensor, event_bus: EventBus):
        self.rangefinder = rangefinder
        self.event_bus = event_bus

    def power_up(self):
        print ("Rangefinder module powering up")
        self.event_bus.register(self, MessageType.RangeCommand)

    def power_down(self):
        self.event_bus.unregister(self.get_name())
        self.rangefinder.close()

    def process(self, message: Message):
        response = Message()
        response.set_payload(5)#self.rangefinder.distance)
        response.set_type(MessageType.RangeResponse)
        self.event_bus.post_message(response)
        
