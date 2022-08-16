from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from WolfXRobot.events import register
from WolfXRobot import ubot2


@register(pattern="^/scheck ?(.*)")
async def _(event):
    chat = "@SpamBot"
    msg = await event.reply("Checking If You Are Limited...")
    async with ubot2.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await ubot2.send_read_acknowledge(chat)
        except YouBlockedUserError:
            await msg.edit("Boss! Please Unblock @SpamBot ")
            return
        await msg.edit(f"~ {response.message.message}")

__help__ = """
*Admins Only Command*
/delall : Reply with message from where all messages should be deleted
*NOTE: Purge can only delete messages sent with 24 hours and purge can only delete 100 messages in single time but /delall can delete whole messages from the starting*
"""
__mod_name__ = "SᴘᴀᴍCʜᴇᴄᴋᴇʀ❌"
