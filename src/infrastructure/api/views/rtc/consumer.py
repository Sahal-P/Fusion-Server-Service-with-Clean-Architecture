from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json


class SignalConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = self.scope["url_route"]["kwargs"]["room_name"]
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = text_data_json["message"]
        action = text_data_json["type"]
        sender = text_data_json["sender"]
        # Handle received data
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "action": action,
                "message": msg,
                "sender": sender,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        action = event["action"]
        sender = event["sender"]
        await self.send(
            text_data=json.dumps(
                {
                    "type": action,
                    "message": message,
                    "sender": sender,
                }
            )
        )

    async def disconnect(self, close_code):
        pass


class UserConnection(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = self.scope["url_route"]["kwargs"]["room_name"]
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        await self.send(
            json.dumps({"Status": "You are now connected to UserConnection Channel."})
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = text_data_json["message"]
        action = text_data_json["type"]
        sender = text_data_json["sender"]
        # Handle received data
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "action": action,
                "message": msg,
                "sender": sender,
            },
        )

    async def chat_message(self, event):
        pass

    async def disconnect(self, close_code):
        await self.send("You have been disconnected.")
