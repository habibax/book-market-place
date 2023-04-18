from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class BooksConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'book_info',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'book_info',
            self.channel_name
        )

    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     await self.send(text_data=json.dumps({
    #         'message': message
    #     }))
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
        except ValueError:
            print(f"Invalid JSON received: {text_data}")
            return

        message = data.get('message')
        if message:
            # Handle the message as needed
            print(f"Received message: {message}")

        title = data.get('title')
        author = data.get('author')
        price = data.get('price')
        if title and author and price:
            # Handle the book info as needed
            print(f"Received book info: {title}, {author}, {price}")
    async def book_info(self, event):
        title = event['title']
        author = event['author']
        price = event['price']

        await self.send(text_data=json.dumps({
            'title': title,
            'author': author,
            'price': str(price)
        }))