from Communication.Server import Server
from Communication.EventBus import EventBus
from Physical.MobilityModule import MobilityModule
from Physical.RangefinderModule import RangefinderModule
from Physical.LedModule import LedModule

from gpiozero import DistanceSensor, Robot, LED
from queue import Queue


q = Queue()
server = Server(q)
event_bus = EventBus()

mobility = MobilityModule(Robot(left = (23, 24, 18), right =(16, 20, 12),))
led = LedModule(LED(37))
rangefinder = RangefinderModule(DistanceSensor(echo = 5, trigger = 6 ,max_distance = 2))

mobility.power_up()
led.power_up()
rangefinder.power_up()

server.start()
event_bus.start()



