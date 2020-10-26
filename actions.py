import json
import pickle

import requests

from  classifier import sanitize_text

class Action:

    
    def is_triggered_by(self, event):
        raise NotImplementedError
    
    @classmethod
    def run(event, event_runner):
        raise NotImplementedError

class WelcomeContributorAction(Action):

    def __init__(self):
        with open("notanewbie.json") as f :
            self.contributors = json.load(f)
        
        with open("trained_classifier.pickle","rb") as f : 
            self.classifier = pickle.load(f)
    
    def is_triggered_by(self, event):

        try: 
            messenger = event['fromUser']['username']
            if messenger in  self.contributors :    
                return False
            
            else:
                is_new =  self.classifier.classify(sanitize_text(event['text']))
                if is_new == "yes" : 
                    return True
            
            return False


        except KeyError:
            return False
    
    def run(self, event, event_runner):
        message = f"""Hi @{event['fromUser']['username']} :)
                   See: https://aboutcode.readthedocs.io/ for more info on how to get started.
                   Additionally, check out the issue pages on our various repos to find things to work on :)
                   """
        event_runner.gitter_client.messages.send(event_runner.room, message)