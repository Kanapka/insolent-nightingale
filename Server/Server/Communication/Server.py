
import asyncio
import threading
import websockets
import json
from .Message import Message

class Server(threading.Thread):
    async def connectionHandler(self, websocket):
        print("Client connected")
        async for recieved in websocket:
            print("Recieved message")
            message = Message(json.loads(recieved))
            self.queue.put(message)

    def __init__(self, _queue):
        threading.Thread.__init__(self)
        self.queue = _queue
        self.initialize = websockets.serve(self.connectionHandler, "127.0.0.1", 443)

    def run(self):
        print("Server starting")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.initialize)
        loop.run_forever()