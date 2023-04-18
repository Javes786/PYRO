import asyncio
import os

os.system('clear')

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"


import pyrogram
from pyrogram import Client
from pyrogram import filters

hehe = b+"""

█▀█ █▄█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█
█▀▀ ░█░ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█

"""
print("hehe")
print("")
print("")
print("")
print(y+"PYROGRAM STRING SESSION GENERATOR")
print(y+"COPYRIGHT © BY @CRIMINAL786")
print(y+"100% SAFE [ TRUSTED ]")
print("")
print(w+"")
APP_ID = int(input("PLEASE ENTER TELEGRAM APP ID: "))
API_HASH = input("PLEASE ENTER TELEGRAM API HASH: ")
with Client(":memory:", api_id=APP_ID, api_hash=API_HASH, in_memory=True) as app:
        app.send_message(
            "me",
            f"STRING_SESSION\n\n`{app.export_session_string()}`**TAP TO COPY**"
        )
        print("Done !, session string has been sent to saved messages!")
print("")
print("")
print("")
print(g+"YOUR DETAILS ARE END TO END ENCRYPTED :)")
print(g+"ENJOY ❤")
