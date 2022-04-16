import random

from telegram import ParseMode
from telethon import Button

from WolfXRobot import OWNER_ID, SUPPORT_CHAT
from WolfXRobot import telethn as tbot

from ..events import register


@register(pattern="/feedback ?(.*)")
async def feedback(e):
    quew = e.pattern_match.group(1)
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    WOLF = (
      "https://telegra.ph/file/9332b113ddb8555bf6ffe.jpg",
      "https://telegra.ph/file/fbc20e462231564a7407f.jpg",
      "https://telegra.ph/file/45df1a2dcf2e385d5cb7b.jpg",
      "https://telegra.ph/file/89e069ddc5c581a3501ef.jpg",
      "https://telegra.ph/file/2d75f08b6da4ac453a500.jpg",
      "https://telegra.ph/file/4b8a6352daa4597e5b507.jpg",
      "https://telegra.ph/file/4ffaff9bb7f3d7818ef21.jpg",
      "https://telegra.ph/file/a62f6de763dbb2b32dace.jpg",
      "https://telegra.ph/file/7c5715131dd0f188e1582.jpg",
      "https://telegra.ph/file/5f8e2c2e0147d8ec4fa86.jpg",
      "https://telegra.ph/file/30dd0b041aaff87826264.jpg",
      "https://telegra.ph/file/9b9de1bd73e482e45d47e.jpg",
      "https://telegra.ph/file/6a1a542b0846bae071a15.jpg",
      "https://telegra.ph/file/6fa7b00d49c8db42f2bb1.jpg",
      "https://telegra.ph/file/f3e0cedf92b3f234cd84f.jpg",
      "https://telegra.ph/file/60998d8f5520b95aec7f9.jpg",
      "https://telegra.ph/file/2d9f1eb3c8ae1980bf9f6.jpg",
      "https://telegra.ph/file/f830ea186d932a076719a.jpg",
      "https://telegra.ph/file/0cde16e55a50dd22715cd.jpg",
      "https://telegra.ph/file/74fc9c85fd341157fee1c.jpg",
      "https://telegra.ph/file/dd8b72e3976d1fd35615a.jpg",
      "https://telegra.ph/file/1b81b3ff11c45e4e31358.jpg",
      "https://telegra.ph/file/be4e82ab2b9de9cb97fb0.jpg",
      "https://telegra.ph/file/58b3cdf9203431ecfce2a.jpg",
)

    NATFEED = ("https://telegra.ph/file/2dd04f407b16bc2cfdf76.jpg",)
    BUTTON = [[Button.url("View Feedback ✨", f"https://t.me/{SUPPORT_CHAT}")]]
    TEXT = "Thanks For Your Feedback, I Hope You Happy With Our Service"
    GIVE = "Give Some Text For Feedback ✨"
    logger_text = f"""
**New Feedback**

**From User:** {mention}
**Username:** @{e.sender.username}
**User ID:** `{e.sender.id}`
**Feedback:** `{e.text}`
"""
    if e.sender_id != OWNER_ID and not quew:
        await e.reply(
            GIVE,
            parse_mode=ParseMode.MARKDOWN,
            buttons=BUTTON,
            file=random.choice(NATFEED),
        ),
        return

    await tbot.send_message(
        SUPPORT_CHAT,
        f"{logger_text}",
        file=random.choice(WOLF),
        link_preview=False,
    )
    await e.reply(TEXT, file=random.choice(WOLF), buttons=BUTTON)
