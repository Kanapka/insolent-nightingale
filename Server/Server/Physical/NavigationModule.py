from Physical.BaseModule import BaseModule
from Physical.RangefinderModule import RangefinderModule
from Communication.EventBus import EventBus
from Communication.Message import Message, MessageType
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
        self.Positon = Position(Environment)

        asyncio.get_event_loop().run_until_complete(self.update_state())
        asyncio.get_event_loop().run_forever()

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

    async def update_state(self):
        while(True):
            print('Updating state')
            sleep(1)

class Environment:
    unknown = 0
    empty = 1
    occupied = -1
    cell_size = 0.02    # in meters
    cell_count = 2000

    def __init__(self):
        self.area = np.zeros((Environment.cell_count, Environment.cell_count), dtype = bool)

class Position: 
    def __init__(self, initial_x: int, initial_y: int):
        self.x = initial_x
        self.y = initial_y
        self.rotation = 0

class Direction: 
    def __init():
        self.x = 0
        self.y = 0









