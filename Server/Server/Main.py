from Communication.Server import Server
from Communication.EventBus import EventBus
from Physical.MobilityModule import MobilityModule
from Physical.RangefinderModule import RangefinderModule
from Physical.LedModule import LedModule

from gpiozero import DistanceSensor, Robot, LED, Device
from gpiozero.pins.mock import MockFactory
from queue import Queue

Device.pin_factory = MockFactory()


q = Queue()
event_bus = EventBus()
event_bus.setQueue(q)
server = Server(q)

#mobility = MobilityModule(Robot(left = (23, 24, 12), right = (16, 20, 13)))
led = LedModule(LED(37))
rangefinder = RangefinderModule(DistanceSensor(echo = 5, trigger = 6 ,max_distance = 2))

#mobility.power_up()
led.power_up()
rangefinder.power_up()

server.start()
event_bus.start()



