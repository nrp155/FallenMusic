import asyncio
import requests
from pyrogram import idle
from pyrogram import Client as Bot

from callsmusic import run
from callmusic.callsmusic import client
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)
await client.join_chat("DevilsHeavenMF")

bot.start()
run()
idle()
