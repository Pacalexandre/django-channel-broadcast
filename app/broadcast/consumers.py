"""Consumer da application broadcast"""
from channels.generic.websocket import AsyncWebsocketConsumer

class JokerConsumer(AsyncWebsocketConsumer):
    async def accept(self):
        await self.channel_layer.group_add('jokes', self.channel_name)
        await self.accept()

    