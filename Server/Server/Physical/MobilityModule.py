from gpiozero import Robot, DistanceSensor, DigitalOutputDevice
from .BaseModule import BaseModule

class MobilityModule(BaseModule):
    def _init_(self):
        self.robot = Robot(left = (23, 24, 18), right =(16, 20, 12),)

    def power_up(self):
        super().power_up()

    def power_down(self):
        pass
        
    def get_name(self):
        return "Mobility"
    
    def process(self, message):
        print(f'Mobility module recieved a message {message["Payload"]}')

    def forward(self):
        self.robot.forward()
        print ("Going forward")

    def reverse(self):
        print ("Reversing")
        self.robot.backward()

    def right(self):
        print ("Turning right");
        self.robot.right()

    def left(self):
        print ("Turning left");
        self.robot.left()

    def stop_moving(self): 
        print ("Stopped moving");
        self.robot.stop()

