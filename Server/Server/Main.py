from Communication.Server import Server
from Communication.EventBus import EventBus
from Physical.MobilityModule import MobilityModule
from Physical.RangefinderModule import RangefinderModule
from Navigation.NavigationModule import NavigationModule

from gpiozero import DistanceSensor, Robot, Device
from gpiozero.pins.mock import MockFactory
import json

configFilePath = "Config/config.json"
modulesConfigFilePath = "Config/modules.json"

with open(configFilePath, 'r') as f:
    CONFIG = json.load(f)
with open(modulesConfigFilePath, 'r') as f:
    MODULES = json.load(f)

if CONFIG['virtualPins']:
    Device.pin_factory = MockFactory()


event_bus = EventBus()
server = Server(event_bus)

leftMotor = (MODULES['mobility']['left']['inputA'], MODULES['mobility']['left']['inputB'], MODULES['mobility']['left']['pwm'])
rightMotor = (MODULES['mobility']['right']['inputA'], MODULES['mobility']['right']['inputB'], MODULES['mobility']['right']['pwm'])
if CONFIG['virtualPins']:
    leftMotor = (MODULES['mobility']['left']['inputA'], MODULES['mobility']['left']['inputB'])
    rightMotor = (MODULES['mobility']['right']['inputA'], MODULES['mobility']['right']['inputB'])

mobility = MobilityModule(Robot(left = leftMotor, right = rightMotor, pwm=False), event_bus)
rangefinder = RangefinderModule(DistanceSensor(echo = MODULES['rangefinder']['echo'], trigger = MODULES['rangefinder']['trigger'] ,max_distance = 2), event_bus)
navigation = NavigationModule(event_bus)

mobility.power_up()
rangefinder.power_up()
#navigation.power_up()

#navigation.environment.dump_to_file()

server.run()























