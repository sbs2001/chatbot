import os

from  chatbot import ChatBot
from  actions import WelcomeContributorAction

token = os.environ.get("GITTER_TOKEN")
room = os.environ.get("GITTER_ROOM")

ChatBot(token, room, [WelcomeContributorAction()])