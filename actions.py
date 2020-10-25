import json

import requests

class Action:

    @staticmethod
    def is_triggered_by(event, event_runner):
        raise NotImplementedError
    
    @classmethod
    def run(event, event_runner):
        raise NotImplementedError

class WelcomeContributorAction(Action):

    def __init__(self):
        with open("notanewbie.json") as f :
            self.contributors = json.load(f)
    
    def is_triggered_by(self, event):

        try: 
            messenger = event['fromUser']['username']
            if messenger in  self.contributors : 
                print("Already contributor")
                return False
            
            else:
                msg_words = set(event['text'].split())
                if "contribute" in msg_words : 
                    print("Noob")
                    return True
                print("Other")
                return False

        except KeyError:
            print("Bad event")
            return False


