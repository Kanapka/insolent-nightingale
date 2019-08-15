from Physical.BaseModule import BaseModule
from Communication.Message import Message, MessageType
from Communication.EventBus import EventBus
from gpiozero import DistanceSensor

class RangefinderModule(BaseModule):
    def __init__(self, rangefinder: DistanceSensor):
        self.rangefinder = rangefinder

    def power_up(self):
        super().power_up()
        EventBus().register(self, MessageType.RangeCommand)

    def power_down(self):
        super().power_down()
        self.rangefinder.close()

    def process(self, message: Message):
        response = Message()
        response.set_payload(self.rangefinder.distance)
        response.set_type(MessageType.RangeResponse)
        bus = EventBus()
        bus.post_message(response)
        
