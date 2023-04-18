import websocket
import json

def on_message(ws, message):
    print(f'Received message: {message}')

def on_error(ws, error):
    print(f'Received error: {error}')

def on_close(ws):
    print('Connection closed')

# def on_open(ws):
#     message = {
#         'type': 'chat.message',
#         'room_name': 'my_room',
#         'message': 'Hello, world!'
#     }
#     ws.send(json.dumps(message))

websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://127.0.0.1:8000/ws/books/",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
# ws.on_open = on_open
ws.run_forever()
