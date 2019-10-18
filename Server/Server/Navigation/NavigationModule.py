from Physical.BaseModule import BaseModule
from Communication.EventBus import EventBus
from Communication.Message import Message, MessageType
from Navigation.Environment import Environment
import threading
from time import sleep
import numpy as np

class NavigationModule(BaseModule):
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.enabled = False
        self.positon = np.array([Environment.cell_count / 2, Environment.cell_count / 2])
        self.rotation = 0.0
        self.environment = Environment()
        self.updater = NavigationUpdater(event_bus)

    def power_up(self):
        print ("Navigation powering up")
        self.enabled = True
        self.event_bus.register(self, MessageType.RangeResponse)
        self.event_bus.register(self, MessageType.DistanceTravelled)
        self.event_bus.register(self, MessageType.RotationPerformed)
        self.event_bus.register(self, MessageType.DumpMap)

        self.updater.start()

    def power_down(self):
        self.updater.stop()
        self.event_bus.unregister(self.get_name())

    def get_name(self):
        return "Navigation module"

    def process(self, message: Message):
        if(message.message_type == MessageType.RangeResponse):
            self.registerContact(message)
        elif message.message_type == MessageType.DistanceTravelled:
            self.registerDistance(message)
        elif message.message_type == MessageType.RotationPerformed:
            self.registerRotation(message)
        elif message.message_type == MessageType.DumpMap:
            self.environment.dump_to_file(self.positon)

    def registerContact(self, message: Message):
        distance = message.payload
        print(f'Contact {distance} away')
        vector = self.heading() * distance
        vector = vector + self.positon
        print(f'Contact at {vector}')
        self.environment.register_obstacle(vector)

    def heading(self):
        return np.array([np.cos(self.rotation), np.sin(self.rotation)])

    def registerRotation(self, message: Message):
        rotation = message.payload
        print(f'Rotated by {rotation}')
        self.rotation += rotation

    def registerDistance(self, message: Message):
        distance = message.payload
        print(f'Travelled {distance}')
        vector = self.heading() * distance
        self.positon += vector

class NavigationUpdater(threading.Thread):
    def __init__(self, bus: EventBus):
        threading.Thread.__init__(self)
        self.event_bus = bus

    def run(self):
        while(True):
            message = Message()
            message.set_type(MessageType.RangeCommand)
            self.event_bus.post_message(message)
            sleep(0.5)

    def stop(self):
        self._stop()










