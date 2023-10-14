import uvicorn
from fastapi import FastAPI, WebSocket
import json

app = FastAPI()


active_connections = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.add(websocket) 
    try:
        while True:
            data = await websocket.receive_text()
            try:
                received_json = json.loads(data)
                response_json = {"message": "Received as JSON format", "data": received_json}
                await websocket.send_text(json.dumps(response_json))
            except json.JSONDecodeError:
                await websocket.send_text(json.dumps({"error": "Invalid JSON format"}))
            except Exception as e:
                await websocket.send_text(json.dumps({"error": str(e)}))
    except:
        active_connections.remove(websocket)  

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
