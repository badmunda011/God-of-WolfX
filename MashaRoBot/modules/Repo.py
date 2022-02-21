import os
from pyrogram import Client, filters
from pyrogram.types import *

from MashaRoBot.conf import get_str_key
from MashaRoBot import pbot
 
 # pls don't delete
REPO_TEXT = "**WolfXRobot [BOT](https://telegra.ph/file/64b39f6e2862e4d91d043.jpg) will Make Your Groups Secured And it's have a lot of fun features (:  ! \n\n↼ Owner ⇀ : 『 [✰ ꫝꪖᥴ𝕜ꫀ𝕣 ✰](t.me/HMF_Owner_1) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @WolfXRobot «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("ʀᴇᴘᴏꜱɪᴛᴏʀʏ", url=f"https://github.com/Thiruselvan999/God-of-Wolf-X"),
        InlineKeyboardButton("Gɪᴛʜᴜʙ", url=f"https://github.com/Thiruselvan999"),
      ],[
        InlineKeyboardButton("ᴏᴡɴᴇʀ ❣️", url="https://t.me/HMF_Owner_1"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/Cringe_Guys_Botz"),
       InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Cringe_Guys_Botz"),
      ],[
        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/Cringe_Guys_Bot"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/AASF_CYBERKING"),
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
