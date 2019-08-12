from .BaseModule import BaseModule

class MobilityModule(BaseModule):
    def get_name(self):
        return "Mobility"
    
    def process(self, message):
        print(f'Mobility module recieved a message {message["Payload"]}')

