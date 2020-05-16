#!/usr/bin/env python3

# Import settings
import config

# Import important modules
import sys
import glob
from telethon import TelegramClient,events

if len(sys.argv) >= 2:
	account_file = sys.argv[1]
else:
	account_file = config.account_file
if len(sys.argv) >= 3:
	chat_id = int(sys.argv[2])
else:
	chat_id = config.chat_id
if len(sys.argv) >= 4:
	path = sys.argv[3]
else:
	path = config.path

client = TelegramClient(account_file, config.api_id, config.api_hash)

async def main():
	files = glob.glob(path + "*.png")
	files.extend(glob.glob(path + "*.jpg"))
	files.extend(glob.glob(path + "*.jpeg"))
	await client.send_file(chat_id, files)

with client:
	client.loop.run_until_complete(main())
