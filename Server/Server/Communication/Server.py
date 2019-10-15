import asyncio
import websockets
import json
from Communication.Message import Message
from Communication.EventBus import EventBus

class Server():
    async def connectionHandler(self, websocket, whatever):
        print("Client connected")
        async for recieved in websocket:
            message = Message(json.loads(recieved))
            self.event_bus.post_message(message)

    def __init__(self, event_bus: EventBus):
        self.initialize = websockets.serve(self.connectionHandler, "0.0.0.0", 443, ping_interval = None)
        self.event_bus = event_bus

    def run(self):
        print("Server starting")
        asyncio.get_event_loop().run_until_complete(self.initialize)
        asyncio.get_event_loop().run_forever()