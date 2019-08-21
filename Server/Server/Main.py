from Communication.Server import Server
from Communication.EventBus import EventBus
from Physical.MobilityModule import MobilityModule
from Physical.RangefinderModule import RangefinderModule
from Physical.NavigationModule import NavigationModule
from Physical.LedModule import LedModule

from gpiozero import DistanceSensor, Robot, LED, Device
from gpiozero.pins.mock import MockFactory
from queue import Queue

Device.pin_factory = MockFactory()


event_bus = EventBus()
server = Server(event_bus)

mobility = MobilityModule(Robot(left = (23, 24, 12), right = (16, 20, 13), pwm=False), event_bus)
led = LedModule(LED(37), event_bus)
rangefinder = RangefinderModule(DistanceSensor(echo = 5, trigger = 6 ,max_distance = 2), event_bus)
navigation = NavigationModule(event_bus)

mobility.power_up()
led.power_up()
rangefinder.power_up()
navigation.power_up()

server.run()



