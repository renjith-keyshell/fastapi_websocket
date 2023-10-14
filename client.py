import asyncio
import websockets
import json

async def send_receive():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter your message (type 'exit' to quit): ")
            if message.lower() == "exit":
                break
            data_to_send = {"message": message}
            await websocket.send(json.dumps(data_to_send))
            print(f"> Sent: {data_to_send}")

            # Receiving JSON response
            response = await websocket.recv()
            print(f"> Received: {response}")

asyncio.get_event_loop().run_until_complete(send_receive())
