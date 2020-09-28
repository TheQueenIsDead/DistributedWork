import json

from channels.generic.websocket import WebsocketConsumer
from . import tasks


class ChatConsumer(WebsocketConsumer):
    def receive(self, text_data):
        # Here we receive some data from the client
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Here we can process client data and send result back directly
        # to the client (by using his unique channel name - `self.channel_name`)
        task.process_client_data_in_the_background_and_send_message_back_to_the_client(self.channel_name, message)

        # And send some result back to that client immediately
        self.send(text_data=json.dumps({'message': 'Your request was received!'}))
