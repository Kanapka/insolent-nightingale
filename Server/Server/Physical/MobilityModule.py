from gpiozero import Robot
from Physical.BaseModule import BaseModule
from Communication.Message import Message, MessageType
from Communication.EventBus import EventBus

class MobilityModule(BaseModule):
    
    forward = "Forward"
    backward = "Backward"
    left = "Left"
    right = "Right"
    stopped = "Stopped"

    def __init__(self, robot: Robot, event_bus: EventBus):
        self.robot = robot
        self.event_bus = event_bus
        self.current = MobilityModule.stopped

    def power_up(self):
        super().power_up()
        self.event_bus.register(self, MessageType.MovementCommand)

    def power_down(self):
        super().power_down()
        self.event_bus.unregister(self.get_name())
        self.robot.close()
        
    def get_name(self):
        return "Mobility"
    
    def process(self, message: Message):
        print(f'Mobility module recieved a message {message.payload}')
        if(message.payload == self.current):
            pass
        else:
            if message.payload == MobilityModule.forward:
                self.forward()
            elif message.payload == MobilityModule.backward:
                self.backward()
            elif message.payload == MobilityModule.left:
                self.left()
            elif message.payload == MobilityModule.right:
                self.right()
            else:
                self.stop_moving()

    def forward(self):
        self.current = MobilityModule.forward
        self.robot.forward()
        print ("Going forward")

    def backward(self):
        self.current = MobilityModule.backward
        print ("Reversing")
        self.robot.backward()

    def right(self):
        self.current = MobilityModule.right
        print ("Turning right")
        self.robot.right()

    def left(self):
        self.current = MobilityModule.left
        print ("Turning left")
        self.robot.left()

    def stop_moving(self): 
        self.current = MobilityModule.stopped
        print ("Stopped moving")
        self.robot.stop()
