from gpiozero import Robot
from Physical.BaseModule import BaseModule
from Communication.Message import Message, MessageType
from Communication.EventBus import EventBus

class MobilityModule(BaseModule):

    def __init__(self, robot: Robot):
        self.robot = robot

    def power_up(self):
        super().power_up()
        EventBus().register(self, MessageType.MovementCommand)

    def power_down(self):
        super().power_down()
        self.robot.close()
        
    def get_name(self):
        return "Mobility"
    
    def process(self, message: Message):
        print(f'Mobility module recieved a message {message.payload}')
        if message.payload == 'Forward':
            self.forward()
        elif message.payload == 'Backward':
            self.backward()
        elif message.payload == 'Left':
            self.left()
        elif message.payload == 'Right':
            self.right()
        else:
            self.stop_moving()

    def forward(self):
        self.robot.forward()
        print ("Going forward")

    def backward(self):
        print ("Reversing")
        self.robot.backward()

    def right(self):
        print ("Turning right")
        self.robot.right()

    def left(self):
        print ("Turning left")
        self.robot.left()

    def stop_moving(self): 
        print ("Stopped moving")
        self.robot.stop()

