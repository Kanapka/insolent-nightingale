from Communication.Server import Server
from queue import Queue
import threading
import asyncio

class Consumer(threading.Thread):
    def __init__(self, _queue):
        threading.Thread.__init__(self)
        self.queue = _queue

    async def consumeSingle(self):
        if(self.queue.empty()):
            await asyncio.sleep(3)
        else:
            while(not self.queue.empty()):
                print("Found message in queue:")
                message = self.queue.get()
                print(message)
                print(message["Module"]["Name"])
                print(message["Payload"])

    async def consume(self):
        while True:
            print("checking for messages")
            await self.consumeSingle()

    def run(self):
        print ("Starting consumer")
        asyncio.run(self.consume())

q = Queue()
server = Server(q)
consumer = Consumer(q)
server.start()
consumer.start()
