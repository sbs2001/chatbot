import requests

class Action:

    @staticmethod
    def is_triggered_by(event, event_runner):
        raise NotImplementedError
    
    @classmethod
    def run(event, event_runner):
        raise NotImplementedError


class StartListeningToGitterRoomAction(Action):

    @staticmethod
    def is_triggered_by(event, event_runner):
        return not getattr(event_runner, "room_updates", None):
    
    @staticmethod
    def run(event, event_runner):
        try: 
            room_id = getattr(event_runner, "room_id")
            gitter_token = getattr(event_runner, "token")

        except AttributeError : 
            raise

        headers = {'Authorization': 'Bearer ' + gitter_token}
        endpoint = f"https://stream.gitter.im/v1/rooms/{room_id}/chatMessages"
        events = requests.get(endpoint, headers=headers, stream=True)

        def room_updates():
            for event in events : 
                if event : 
                    yield event

        setattr(event_runner, "room_updates", room_updates)






