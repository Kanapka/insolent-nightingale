
import asyncio
import threading
import websockets
import logging
import json

class Server(threading.Thread):
    async def connectionHandler(self, websocket, path):
        print("Client connected")
        async for message in websocket:
            print("Recieved message")
            data = json.loads(message)
            self.queue.put(data)

    def __init__(self, _queue):
        threading.Thread.__init__(self)
        self.queue = _queue

    def run(self):
        print("Server starting")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.initialize = websockets.serve(self.connectionHandler, "127.0.0.1", 443)
        loop.run_until_complete(self.initialize)
        loop.run_forever()