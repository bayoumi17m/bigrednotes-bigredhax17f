#!/usr/bin/env python
from twilio.rest import Client
import youtube_search
import shutil
import os
import glob
import clutch

# Your Account SID from twilio.com/console
account_sid = "AC97fcc021ec3dd5847e15421ede53b9eb"
# Your Auth Token from twilio.com/console
auth_token  = "437bf7e23575b3a957dbbe0435384e86"

client = Client(account_sid, auth_token)

with open('/Applications/XAMPP/xamppfiles/htdocs/data.txt', 'r') as f:
        numberText = f.read()

message = client.messages.create(
    to=numberText, 
    from_="+14696208610",
    body=youtube_search.handle_video_search(clutch.justDoIt()))

print(message.sid)

print(" ")