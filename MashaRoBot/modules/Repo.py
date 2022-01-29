import os
from pyrogram import Client, filters
from pyrogram.types import *

from MashaRoBot.conf import get_str_key
from MashaRoBot import pbot
 
 # pls don't delete
REPO_TEXT = "**WolfXRobot [BOT](https://telegra.ph/file/526ed899597d7827474a1.jpg) will Make Your Groups Secured And it's have a lot of fun features (:  ! \n\n↼ Owner ⇀ : 『 [Telegram pro](t.me/HMF_Owner_1) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @WolfXRobot «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("ʀᴇᴘᴏꜱɪᴛᴏʀʏ", url=f"https://github.com/Thiruselvan999/God-of-Wolf-X"),
        InlineKeyboardButton("Gɪᴛʜᴜʙ", url=f"https://github.com/Thiruselvan999"),
      ],[
        InlineKeyboardButton("ᴏᴡɴᴇʀ ❣️", url="https://t.me/HMF_Owner_1"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/Stuxnet_1_official"),
       InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/stuxnetBotz"),
      ],[
        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/THANIMAIBOTS"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/AASFCYBERKING"),
       InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Awesome_Prince"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
