import csv
import os

import requests

gitter_token = os.environ["GITTER_TOKEN"]
gitter_room_id = os.environ["GITTER_ROOM_ID"]
params = ""
messages = []

while True : 
    try:
        ur = f"https://api.gitter.im/v1/rooms/{gitter_room_id}/chatMessages?{params}access_token={gitter_token}"
        resp = requests.get(ur).json()
        params = f'beforeId={resp[0]["id"]}&'
        messages.extend(
            [
            mes["text"] for mes in resp
            ]
        )
    except:
        break


with open(f'{gitter_room_id}.csv', 'w') as f : 
    writer = csv.writer(f)
    for mes in  messages:
        writer.writerow([mes,"no"])