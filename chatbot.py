import json

import requests
from gitterpy.client import GitterClient


class AboutCodeChatBot:

    def __init__(self, token, room_address, actions):
        self.gitter_client = GitterClient(token=token)
        self.room = room_address 
        self.actions = actions
        start_listening_for_events(self)
        for event in  self.room_updates():
            print(event)
            for action in actions : 
                if action.is_triggered_by(event):
                    action.run(event)
    
def start_listening_for_events(event_runner):
    events = event_runner.gitter_client.stream.chat_messages(event_runner.room)
    def room_updates():
        for event in events.iter_lines() : 
            if event :
                try : 
                    data = json.loads(event)
                    yield data
                
                except json.decoder.JSONDecodeError : 
                    pass 
                
                
    setattr(event_runner, "room_updates", room_updates)
    