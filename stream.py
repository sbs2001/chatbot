import requests

ROOM_ID = "5f943f1ed73408ce4ff25fb7"
TOKEN = "f659583a58291ce7361d1ec00d773719a018893c"

headers = {'Authorization': 'Bearer ' + TOKEN}
endpoint = f"https://stream.gitter.im/v1/rooms/{ROOM_ID}/chatMessages"

resp = requests.get(endpoint, headers=headers, stream=True)
for stream_messages in resp.iter_lines():
    if stream_messages:
        print(stream_messages)

