import asyncio
import time

from WolfXRobot import bot
from pyrogram import filters
from pyrogram.types import Message

@bot.on_message(filters.command("obama", ['/', ".", "?"]))
async def status(bot, m: Message):
    msg = await m.reply("Conecting to Wolf X System System.")
    time.sleep(1)
    await msg.edit("Initialising ✦✧✧✧✧✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✧✧✧✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✦✧✧✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✦✦✧✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✦✦✦✧")
    time.sleep(1)
    await msg.edit("Initialising ✦✦✦✦✦✦")
    time.sleep(1)
    await msg.edit("✪VᴇRɪFɪᴇD✪")
    time.sleep(2)

__mod_name__ = "obama📝"

__help__ = """
 ~ /obama *:* Get Your verified or not. 
"""

