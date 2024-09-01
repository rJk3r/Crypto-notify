# This is a sample Python app for work with telegram notifications

# Developed by rJk3r

# Telethon library to connect app with telegram

from xmlrpc.client import DateTime
from telethon.sync import TelegramClient

from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputPeerChat

import time # Time library for send timestamp


import os
import sys
os.chdir(sys.path[0])

# App style and GUI import
from App import *
from config import api_id, api_hash, phone, limit #import user data

chat_id = 1234567890 # Set your chat_id to get the message

def startUserAuthorization():
    print("autorize")
    pass

def onAppLoad(api_id, api_hash, phone):
    if (type(api_id) is str and type(api_id) is str and type(phone) is str): # Here we check the config data
        try:

            client = TelegramClient(phone, api_id, api_hash) # initialize a telegram client
            time.sleep(1) # Delay for debug
            client.connect()  # start client
            if not client.is_user_authorized():
                #client.send_code_request(phone)
                App().renderUnathorizedCanvas()
                #client.sign_in(phone, input("Введите код: "))
        except Exception as err:
            time.sleep(2) # Delay to send error
            print("[ERROR]: ", err) # raise exception if you have troubles with authorizaion or client initialization
            App.renderUnathorizedCanvas(self=app)
    else:
        print("[ERROR]: Неверно указаны данные api_id, api_hash, или phone") # You have bad API data or phone data


def getChatHistory(client):
    all_messages = []
    all_messages.extend(client(GetHistoryRequest(
        peer=InputPeerChat(chat_id),
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=limit,
        reverse=True
    )))
    return all_messages

def sendHistoryToApp(all_messages, client):
    for message in all_messages:
        # Get message data (Timestamp, text and message authors)
        if message.message:
            if isinstance(message.sender_id, int):
                user = client.get_input_entity(message.sender_id)
            else:
                user = message.sender

            sender = user.first_name + " " + user.last_name if user.last_name else user.first_name
            date = message.date.strftime("%Y-%m-%d %H:%M:%S")
            message_text = message.message

            # writer.writerow([date, sender, message_text])



# Press the green button in the App to run the script.
if __name__ == '__main__':
    app = App() # Get App class

    onAppLoad(api_id, api_hash, phone)
    print(type(app))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
