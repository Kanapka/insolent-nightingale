from Communication.Server import Server
from Communication.EventBus import EventBus
from Physical.MobilityModule import MobilityModule
from Physical.LedModule import LedModule
from queue import Queue
import threading
import asyncio


q = Queue()
server = Server(q)
event_bus = EventBus(q)

mobility = MobilityModule()
led = LedModule()

event_bus.register(mobility)
event_bus.register(led)

server.start()
event_bus.start()

