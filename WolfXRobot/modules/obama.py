from typing import List
from telethon import custom, events
import os,re
import asyncio
from telegram import Update
from telegram.ext import run_async,CallbackContext
import time
from WolfXRobot.events import register
WolfXRobot import telethn as tgbot
from pyrogram import filters
from WolfXRobot import dispatcher
from WolfXRobot import telethn as bot
from WolfXRobot.modules.disable import DisableAbleCommandHandler

@register(pattern="/obama")
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

