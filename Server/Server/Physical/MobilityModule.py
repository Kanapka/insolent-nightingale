from .BaseModule import BaseModule

class MobilityModule(BaseModule):
    def get_name(self):
        return "Mobility"
    
    def process(self, message):
        print(f'Mobility module recieved a message {message["Payload"]}')

    def forward(self):
        print ("Going forward")

    def reverse(self):
        print ("Reversing")

    def right(self):
        print ("Turning right");

    def left(self):
        print ("Turning left");

    def stop_moving(self): 
        print ("Stopped moving");

