from Communication.Server import Server
from queue import Queue
import threading
import asyncio

class EventBus(threading.Thread):
    def __init__(self, _queue):
        threading.Thread.__init__(self)
        self.queue = _queue
        self.registered_listeners = dict()

    def process_messages(self):
        while(not self.queue.empty()):
            message = self.queue.get()
            print(f'Found message in queue')
            for key in filter(lambda x: x == message['Module']['Name'], self.registered_listeners):
                self.registered_listeners[key].process(message)

    async def loop(self):
        while True:
            if(self.queue.empty()):
                await asyncio.sleep(0.05)
            else:
                self.process_messages()

    def register(self, listener):
        self.registered_listeners[listener.get_name()] = listener

    def unregister(self, listener_name):
        self.registered_listeners.pop(listener_name, 'default');

    def post_message(self, message):
        self.queue.put(message)

    def run(self):
        print ("Starting consumer")
        asyncio.run(self.loop())

