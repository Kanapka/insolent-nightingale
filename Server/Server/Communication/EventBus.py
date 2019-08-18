from Communication.Message import Message
from Physical.BaseModule import BaseModule
from time import sleep
from queue import Queue
import threading
import asyncio

class EventBus(threading.Thread):

    __instance = None

    #def __new__(cls):
    #    if EventBus.__instance is None:
    #        EventBus.__instance = threading.Thread.__new__(cls)
    #    return EventBus.__instance

    def __init__(self):
        self.registered_listeners = list()

    def register(self, module: BaseModule, message_type: str):
        self.registered_listeners.append(Listener(module, message_type))

    def unregister(self, listener_name: str):
        self.registered_listeners = filter(lambda x: x.module.get_name() != listener_name, self.registered_listeners)

    def post_message(self, message: Message):
        for listener in filter(lambda x: x.message_type == message.message_type, self.registered_listeners):
            listener.module.process(message)

class Listener: 
    def __init__(self, module: BaseModule, messsage_type: str):
        self.module = module
        self.message_type = messsage_type