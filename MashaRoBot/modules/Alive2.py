# This file is part of @WolfXRobot (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# Give Credits To @HMF_OWNER_1 I Really Hard Worked For This Module 
# Gib Credits Else Gay

import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from mrjoker.events import register
from mrjoker import telethn as borg
from mrjoker import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/e5595c7ec4f67de3852a0.jpg"
file2 = "https://telegra.ph/file/7d3ae207442f9f40fd3b6.jpg"
file3 = "https://telegra.ph/file/3122ebf3bb5e979a131cc.jpg"
file4 = "https://telegra.ph/file/8e99eaa89b4acce19eb31.jpg"
file5 = "https://telegra.ph/file/f0a8494898ea88e99a131.jpg"
file6 = "https://telegra.ph/file/aa9bc9f6c3c00c34827ec.jpg"
file7 = "https://telegra.ph/file/ad8a65d87760b9d0195c1.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=(".alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    await yes.delete()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    pm_caption = "** 🐺⃝ᴳᵒᵈ𝄞ƠƑ ωσℓƒ ✗ 𝑖𝑠 𝑜𝑛𝑙𝑖𝑛𝑒  **\n\n"
    pm_caption += "**𝑰 𝑨𝒎 𝑨𝒍𝒊𝒗𝒆 𝑻𝒊𝒍𝒍 𝒀𝒐𝒖 𝑺𝒖𝒑𝒑𝒐𝒓𝒕𝒊𝒏𝒈...**\n\n"
    pm_caption += "✘ 𝙰𝚋𝚘𝚞𝚝 𝚖𝚎 ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ `{version.__version__}`\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/joinchat/r9qx47U5xEZjY2E1)\n"
    pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [ᴡᴏʟғ ✘ sᴜᴘᴘᴏʀᴛ](https://t.me/HMf_family_offical)\n"
    pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [『 𝙆𝙄𝙎𝙃𝙊𝙍𝙀™』](https://t.me/AASFCYBERKING)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ `{uptime}`\n\n"
    pm_caption += f"➾ **ᴍʏ Owner💝** ☞ [★ Hᴀᴄᴋᴇʀ ★](http://t.me/HMF_OWNER_1)\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

__mod_name__ = "Alive🤖"

__help__ = """
 ~ .alive *:* Get A Alive Message Like Userbot. 
Credits @Horimaya
"""
    
