import requests


class AboutCodeChatBot:

    def __init__(self, token, room_ids, actions):
        self.token = token
        self.room_ids = room_ids
        self.actions = actions
        self.start_listening()
        for event in  self.event_updates():
            for action in actions : 
                if action.is_triggered_by(event):
                    action.run(event)
    
    def start_listening(self):
        headers = {'Authorization': 'Bearer ' + self.token}
        endpoint = f"https://stream.gitter.im/v1/rooms/{self.room_id}/chatMessages"
        self.current_status = requests.get(endpoint, stream=True)
    
    def event_updates(self):
        if not getattr(self, "current_events", None):
            self.start_listening()

        for event in self.current_status.iter_lines():
            if event : 
                yield event

    
    def 
