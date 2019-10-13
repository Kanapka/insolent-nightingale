from Communication import Message

class BaseModule:

    def power_up(self):
        print(f'Module {self.get_name()} powering up')

    def power_down(self):
        print(f'Module {self.get_name()} powering down')

    def process(self, message: Message):
        print(f'Module {self.get_name()} processing message {message}')

    def get_name(self):
        return "Base module"
