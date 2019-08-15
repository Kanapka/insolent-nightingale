class Message:
    def __init__(self, dictionary: dict = None):
        self.message_type = ""
        self.payload = ""
        if dictionary != None:
            self.message_type = dictionary["Type"]
            self.payload = dictionary ["Payload"]

        def set_type(type: str):
            self.message_type = type

        def set_payload(payload):
            self.payload = payload

class MessageType:
    MovementCommand = "MovementCommand"
    LedCommand = "LedCommand"
    RangeCommand = "RangeCommand"
    RangeResponse = "RangeResponse"
