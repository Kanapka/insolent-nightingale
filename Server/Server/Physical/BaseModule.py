class BaseModule:
    def process(self, message):
        print(f'Module {self.name} processing message {message}')

    def get_name(self):
        return "Base module"
