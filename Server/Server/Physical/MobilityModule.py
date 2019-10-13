from gpiozero import Robot
from Physical.BaseModule import BaseModule
from Communication.Message import Message, MessageType
from Communication.EventBus import EventBus
import threading
import time

class MobilityModule(BaseModule):
    
    forward_state = "Forward"
    backward_state = "Backward"
    left_state = "Left"
    right_state = "Right"
    stopped_state = "Stopped"

    def __init__(self, robot: Robot, event_bus: EventBus):
        self.robot = robot
        self.event_bus = event_bus
        self.current = MobilityModule.stopped_state
        self.updater = MovementUpdater(event_bus)

    def power_up(self):
        super().power_up()
        self.event_bus.register(self, MessageType.MovementCommand)
        self.updater.start()

    def power_down(self):
        super().power_down()
        self.event_bus.unregister(self.get_name())
        self.updater.stop()
        self.robot.close()
        
    def get_name(self):
        return "Mobility"
    
    def process(self, message: Message):
        print(f'Mobility module recieved a message {message.payload}')
        self.updater.post_movement(message.payload)
        if(message.payload == self.current):
            pass
        else:
            if message.payload == MobilityModule.forward_state:
                self.forward()
            elif message.payload == MobilityModule.backward_state:
                self.backward()
            elif message.payload == MobilityModule.left_state:
                self.left()
            elif message.payload == MobilityModule.right_state:
                self.right()
            else:
                self.stop_moving()

    def forward(self):
        self.current = MobilityModule.forward_state
        self.robot.forward()
        print ("Going forward")

    def backward(self):
        self.current = MobilityModule.backward_state
        print ("Reversing")
        self.robot.backward()

    def right(self):
        self.current = MobilityModule.right_state
        print ("Turning right")
        self.robot.right()

    def left(self):
        self.current = MobilityModule.left_state
        print ("Turning left")
        self.robot.left()

    def stop_moving(self): 
        self.current = MobilityModule.stopped_state
        print ("Stopped moving")
        self.robot.stop()

class MovementUpdater(threading.Thread):
    Speed = 1 #meters per second
    RotationSpeed = 1 #radian per second

    def __init__(self, bus: EventBus):
        threading.Thread.__init__(self)
        self.event_bus = bus
        self.last_state = MobilityModule.stopped_state
        self.last_state_change = time.time()

    def post_movement(self, new_state):
        message = Message()
        duration = time.time() - self.last_state_change
        self.last_state_change = time.time()
        if self.last_state == MobilityModule.stopped_state: 
            pass
        elif self.last_state == MobilityModule.left or self.last_state == MobilityModule.right:
            message.set_type(MessageType.RotationPerformed)
            payload = duration * MovementUpdater.RotationSpeed
            if self.last_state == MobilityModule.left:
                payload = -payload
            message.set_payload(payload)
            self.event_bus.post_message(message)
        else:
            message.set_type(MessageType.DistanceTravelled)
            payload = duration * MovementUpdater.Speed
            message.set_payload(payload)
            self.event_bus.post_message(message)

        self.last_state = new_state

    def run(self):
        while(True):
            self.post_movement(self.last_state)
            time.sleep(0.5)

    def stop(self):
        self._stop()
            