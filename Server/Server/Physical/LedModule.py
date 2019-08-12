from .BaseModule import BaseModule

class LedModule(BaseModule):
    def get_name(self):
        return "LedModule"

    def process(self, message):
        print(f'Led module recieved a message {message["Payload"]}')
