import asyncio
import os

os.system('clear')

import pyrogram
from pyrogram import Client
from pyrogram import filters

hehe = """

█▀█ █▄█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█
█▀▀ ░█░ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█

"""
print ("hehe")

print("")
print("")
print("")
APP_ID = int(input("PLEASE ENTeR Telegram APP ID: "))
API_HASH = input("PLEASE ENTeR Telegram API HASH: ")
with Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as app:
        app.send_message(
            "me",
            f"#STRING_SESSION\n\n```{app.export_session_string()}``` **TAP TO COPY**"
        )
        print("Done !, session string has been sent to saved messages!")
