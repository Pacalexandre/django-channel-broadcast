"""Consumer da application broadcast"""
from channels.generic.websocket import AsyncWebsocketConsumer

class JokerConsumer(AsyncWebsocketConsumer):
    """Consumer do celery que é responsável pelo envio
     de menssagens Asyncronous para os grupos de """

    async def connect(self):
        await self.channel_layer.group_add('jokes', self.channel_name)
        await self.accept()

    async def disconnect(self, code=None):
        await self.channel_layer.group_discard('jokes', self.channel_name)

    async def send_jokes(self, event):
        """Envio de mensagens para os sockets
        Args:
            event (AsyncWebsocket): montar mensagens para asyncronous para sockets
        """
        text_message = event['text']
        await self.send(text_message)
        