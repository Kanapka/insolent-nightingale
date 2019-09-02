from Physical.BaseModule import BaseModule
from Physical.RangefinderModule import RangefinderModule
from Communication.EventBus import EventBus
from Communication.Message import Message, MessageType
from Navigation.Environment import Environment, Position
import threading
from time import sleep
import asyncio
import numpy as np

class NavigationModule(BaseModule):
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus

    def power_up(self):
        print ("Navigation powering up")
        self.event_bus.register(self, MessageType.RangeResponse)
        self.event_bus.register(self, MessageType.DistanceTravelled)
        self.event_bus.register(self, MessageType.RotationPerformed)
        self.environment = Environment()
        self.positon = Position(Environment.cell_count / 2, Environment.cell_count / 2)

        self.updater = NavigationUpdater()
        self.updater.set_event_bus(self.event_bus)
        self.updater.start()

    def power_down(self):
        self.event_bus.unregister(self.get_name())

    def get_name(self):
        return "Navigation module"

    def process(self, message: Message):
        print (f'Navigation recieved message: {message.payload} ')
        if(message.message_type is MessageType.RangeResponse):
            self.registerContact(message)
        elif message.message_type is MessageType.DistanceTravelled:
            self.registerDistance(message)
        elif message.message_type is MessageType.RotationPerformed:
            self.registerRotation(message)

    def registerDistance(self, message: Message):
        pass

    def registerRotation(self, message: Message):
        pass

    def registerContact(self, message: Message):
        pass

class NavigationUpdater(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event_bus = None
class NavigationUpdater(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event_bus = None

    def set_event_bus(self, bus: EventBus):
        self.event_bus = bus

    def run(self):
        while(True):
            print ('Updating')
            message = Message()
            message.set_payload("lol")
            message.set_type(MessageType.RangeCommand)
            self.event_bus.post_message(message)
            sleep(1)










