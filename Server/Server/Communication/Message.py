class Message:
    def __init__(self, dictionary: dict = None):
        self.message_type = ""
        self.payload = ""
        if dictionary != None:
            self.message_type = dictionary["Type"]
            self.payload = dictionary["Payload"]

    def set_type(self, message_type: str):
        self.message_type = message_type

    def set_payload(self, payload):
        self.payload = payload

class MessageType:
    MovementCommand = "MovementCommand"
    LedCommand = "LedCommand"
    RangeCommand = "RangeCommand"
    RangeResponse = "RangeResponse"
    DistanceTravelled = "DistanceTravelled"
    RotationPerformed = "RotationPerformed"
