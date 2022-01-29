import importlib
import time
import re
import random
from sys import argv
from typing import Optional
import MashaRoBot.modules.sql.users_sql as sql
import MashaRoBot.modules.sql.users_sql as sql
from MashaRoBot import (ALLOW_EXCL, CERT_PATH, DONATION_LINK, LOGGER,
                          OWNER_ID, PORT, SUPPORT_CHAT, TOKEN, URL, WEBHOOK,
                          SUPPORT_CHAT, dispatcher, StartTime, telethn, updater, pbot)

# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from MashaRoBot.modules import ALL_MODULES
from MashaRoBot.modules.helper_funcs.chat_status import is_user_admin
from MashaRoBot.modules.helper_funcs.misc import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


PM_START_TEXT = """
      🦋⃟ƓƠƊ ƠƑ ωοℓƒ ✗ 𝄞✿‌᭄

◈ I am called [ωοℓƒ-✗](https://t.me/wolfxrobot)
◈ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴛᴏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴇxᴘʟᴏsɪᴠᴇ.
┏━━━━━━━━━━━━━━━━━━━━━ 
┃➪ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ Hᴀᴄᴋᴇʀ ғᴏʀ ᴀɴʏ 
┃ǫᴜᴇʀʏ ᴀɴᴅ [Hᴀᴄᴋᴇʀ](https://t.me/HMF_OWNER_1) ʜᴇʀᴇ.
┃➪ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ʜᴇʟᴘ ᴛᴏ ┃ᴇxᴘʟᴏʀᴇ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ ᴀɴᴅ ᴍʏ ┃ғᴇᴀᴛᴜʀᴇs.
┗━━━━━━━━━━━━━━━━━━━━━
➪ Pᴏᴡᴇʀᴇᴅ ʙʏ [𝐰𝐨𝐥𝐟 - 𝐗](https://t.me/joinchat/r9qx47U5xEZjY2E1)
"""

buttons = [
    [
        InlineKeyboardButton(
            text="☑️ฬ๏lŦ ✗ t๏ ץ๏ยг Gɾ๏υρ☑️", url="t.me/WolfXRobot?startgroup=true"),
    ],
    [
        InlineKeyboardButton(
            text="🚨ℓοgѕ🚧", url="https://t.me/stuxnet_logs"),
        InlineKeyboardButton(
            text="🧨ѕυρρ๏яτ🎈", url="https://t.me/Stuxnet_1_official"),
    ],
    [
        InlineKeyboardButton(
            text="⚡нєℓρ & ϲοммєиτѕ🌟", url="https://t.me/Alexa1Robot?start=help"),
    ],
    [
        InlineKeyboardButton(
            text="🤖υρ∂ατєѕ🐺", url="https://t.me/stuxnetBotz"),
        InlineKeyboardButton(
            text="🍿мονιєѕ💎", url="https://t.me/joinchat/r9qx47U5xEZjY2E1"),
    ],
    [
        InlineKeyboardButton(
            text="👑οωиєя🦁", url="https://t.me/HMF_OWNER_1"
    ),
    ],
]


SECOND_START_MSG = """
*Hᴇʟʟᴏ {}!,*
◈ *Sᴇʟᴇᴄᴛ Aʟʟ Cᴏᴍᴍᴀɴᴅs Fᴏʀ Fᴜʟʟ Hᴇʟᴘ Aɴᴅ Dᴏɴ'ᴛ Fᴏʀɢᴇᴛ Tᴏ Aᴅᴅ Mᴇ* [😉](https://telegra.ph/file/9332b113ddb8555bf6ffe.jpg) 
"""

buutons = [
    [
                        InlineKeyboardButton(
                            text="Add Me ➕",
                            url="https://t.me/WolfXRobot?startgroup=true"),
                    ],
                   [
                        InlineKeyboardButton(
                            text="Close ❌",
                            callback_data="cutiipii_back"),
                        InlineKeyboardButton(text="Help 🔐", callback_data="help_back"),
                    ], 
    ]

                    
HELP_STRINGS = """
► 🦋⃟ƓƠƊ ƠƑ ωοℓƒ ✗ 𝄞✿‌᭄ ◄
────────────────────────
➣ Tᴏ ᴍᴀᴋᴇ ᴍᴇ ғᴜɴᴄᴛɪᴏɴᴀʟ, ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ɪ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ɪɴ ʏᴏᴜʀ Gʀᴏᴜᴘ.
➣ /start[:](https://telegra.ph/file/01391f345be099ff7b3dd.jpg) Sᴛᴀʀᴛs ᴍᴇ! Yᴏᴜ'ᴠᴇ ᴘʀᴏʙᴀʙʟʏ ᴀʟʀᴇᴀᴅʏ ᴜsᴇᴅ ᴛʜɪs.
➣ Fᴀᴄɪɴɢ ᴀɴʏ ɪssᴜᴇ ᴏʀ ғɪɴᴅ ᴀɴʏ ʙᴜɢs ɪɴ ᴀɴʏ ᴄᴏᴍᴍᴀɴᴅ ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ʀᴇᴘᴏʀᴛ ɪᴛ ɪɴ [Sᴜᴘᴘᴏʀᴛ](https://t.me/Stuxnet_1_official) Oʀ [Hᴇʀᴇ](http://t.me/hmf_owner_1)
────────────────────────
©️ Wolf X Bot | 2021 - 2022 | [Hacker](http://t.me/HMF_owner_1)
""".format(
    dispatcher.bot.first_name,""
    if not ALLOW_EXCL else "\nAll commands can either be used with / or !.\nKindly use ! for commands if / is not working\n")

RANGER_IMG = (
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

TEXXT = ( "*Hey* [{}](tg://settings/), *You Know That Wolf Never Gives, Born Since:* `{}`", "*Hey* [{}](tg://settings/), *Wolf Came for you! Since:* `{}`", )

RANGER_COMBOT_IMG = "https://telegra.ph/file/dd8b72e3976d1fd35615a.jpg"

DONATE_STRING = """иσ ι иєє∂ ι ¢αи ℓινє ωιтнσυт αиу ∂σиαтισи, ѕтιℓℓ ιи ∂σиαтισи נυѕт נσιи συя [¢нαт](t.me/TRCrazyBots)"""

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
GDPR = []
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("MashaRoBot.modules." +
                                              module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception(
            "Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)
       
    if hasattr(imported_module, "__gdpr__"):
        GDPR.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


# do not async
def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    dispatcher.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=keyboard)


@run_async
def test(update: Update, context: CallbackContext):
    # pprint(eval(str(update)))
    # update.effective_message.reply_text("Hola tester! _I_ *have* `markdown`", parse_mode=ParseMode.MARKDOWN)
    update.effective_message.reply_text("This person edited a message")
    print(update.effective_message)


@run_async
def start(update: Update, context: CallbackContext):
    args = context.args
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_STRINGS)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split('_', 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id, HELPABLE[mod].__help__,
                    InlineKeyboardMarkup([[
                        InlineKeyboardButton(
                            text="Back", callback_data="help_back")
                    ]]))
            elif args[0].lower() == "markdownhelp":
                IMPORTED["extras"].markdown_help_sender(update)
            elif args[0].lower() == "disasters":
                IMPORTED["disasters"].send_disasters(update)
            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(
                        match.group(1), update.effective_user.id, False)
                else:
                    send_settings(
                        match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name
            update.effective_message.reply_photo(
                random.choice(RANGER_IMG),
                PM_START_TEXT.format(
                    escape_markdown(first_name),
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),                        
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=5,
                   )
    else:
        first_name = update.effective_user.first_name
        update.effective_message.reply_photo(
                random.choice(RANGER_IMG), caption=random.choice(TEXXT).format(
                first_name,
                uptime
            ),
            
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                  [                  
                       InlineKeyboardButton(
                             text="👥 Support",
                             url=f"https://t.me/Stuxnet_1_official"),
                       InlineKeyboardButton(
                             text="📢 Updates",
                             url="https://t.me/stuxnetBotz")
                     ] 
                ]
            ),
        )

# for test purposes
def error_callback(update: Update, context: CallbackContext):
    error = context.error
    try:
        raise error
    except Unauthorized:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors


@run_async
def help_button(update, context):
    query = update.callback_query
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = ("Here is the help for the *{}* module:\n".format(
                HELPABLE[module].__mod_name__) + HELPABLE[module].__help__)
            query.message.edit_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        text="Back", callback_data="help_back")
                ]]))

        elif prev_match:
            curr_page = int(prev_match.group(1))
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, HELPABLE, "help")))

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, HELPABLE, "help")))

        elif back_match:
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, HELPABLE, "help")))

        # ensure no spinny white circle
        context.bot.answer_callback_query(query.id)
        # query.message.delete()

    except BadRequest:
        pass


@run_async
def cutiepii_callback_data(update, context):
    query = update.callback_query
    bot = context.bot
    uptime = get_readable_time((time.time() - StartTime))
    if query.data == "cutiepii_":
        query.message.edit_text(
            text="""CallBackQueriesData Here""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="[► Back ◄]", callback_data="cutiepii_back")
                 ]
                ]
            ),
        )
    elif query.data == "cutiepii_back":
        first_name = update.effective_user.first_name
        query.message.edit_text(
                SECOND_START_MSG.format(
                    escape_markdown(first_name),
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),
                reply_markup=InlineKeyboardMarkup(buutons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=5,
                disable_web_page_preview=False,
        )

@run_async
def cutiipii_callback_data(update, context):
    query = update.callback_query
    bot = context.bot
    uptime = get_readable_time((time.time() - StartTime))
    if query.data == "cutiipii_":
        query.message.edit_text(
            text="""CallBackQueriesData Here""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="[► Back ◄]", callback_data="cutiipii_back")
                 ]
                ]
            ),
        )
    elif query.data == "cutiipii_back":
        first_name = update.effective_user.first_name
        query.message.delete()(
                SECOND_START_MSG.format(
                    escape_markdown(first_name),
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),
                reply_markup=InlineKeyboardMarkup(buutons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=5,
                disable_web_page_preview=False,
        )

@run_async
def get_help(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
            module = args[1].lower()
            update.effective_message.reply_photo(
            RANGER_COMBOT_IMG, f"Oh Hey, Click the Button Below to get help of {module.capitalize()}",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        text="click here",
                        url="t.me/{}?start=ghelp_{}".format(
                            context.bot.username, module))
                ]]))
            return

        update.effective_message.reply_photo(
            RANGER_COMBOT_IMG, caption= "Oh Ranger, Click the Button Below to get the list of possible commands.",
            reply_markup=InlineKeyboardMarkup(
                [
                  [
                  InlineKeyboardButton(text=" Click here", url="https://t.me/WolfXRobot?start=help")
                  ]
                ]
            ),
        )
        return

    elif len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
        module = args[1].lower()
        text = "Here is the available help for the *{}* module:\n".format(HELPABLE[module].__mod_name__) \
               + HELPABLE[module].__help__
        send_help(
            chat.id, text,
            InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Back",
                                       callback_data="help_back")]]))

    else:
        send_help(chat.id, HELP_STRINGS)


def send_settings(chat_id, user_id, user=False):
    if user:
        if USER_SETTINGS:
            settings = "\n\n".join("*{}*:\n{}".format(
                mod.__mod_name__, mod.__user_settings__(user_id))
                                   for mod in USER_SETTINGS.values())
            dispatcher.bot.send_message(
                user_id,
                "These are your current settings:" + "\n\n" + settings,
                parse_mode=ParseMode.MARKDOWN)

        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any user specific settings available :'(",
                parse_mode=ParseMode.MARKDOWN)

    else:
        if CHAT_SETTINGS:
            chat_name = dispatcher.bot.getChat(chat_id).title
            dispatcher.bot.send_message(
                user_id,
                text="Which module would you like to check {}'s settings for?"
                .format(chat_name),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)))
        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any chat settings available :'(\nSend this "
                "in a group chat you're admin in to find its current settings!",
                parse_mode=ParseMode.MARKDOWN)


@run_async
def settings_button(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.effective_user
    bot = context.bot
    mod_match = re.match(r"stngs_module\((.+?),(.+?)\)", query.data)
    prev_match = re.match(r"stngs_prev\((.+?),(.+?)\)", query.data)
    next_match = re.match(r"stngs_next\((.+?),(.+?)\)", query.data)
    back_match = re.match(r"stngs_back\((.+?)\)", query.data)
    try:
        if mod_match:
            chat_id = mod_match.group(1)
            module = mod_match.group(2)
            chat = bot.get_chat(chat_id)
            text = "*{}* has the following settings for the *{}* module:\n\n".format(escape_markdown(chat.title),
                                                                                     CHAT_SETTINGS[module].__mod_name__) + \
                   CHAT_SETTINGS[module].__chat_settings__(chat_id, user.id)
            query.message.reply_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        text="Back",
                        callback_data="stngs_back({})".format(chat_id))
                ]]))

        elif prev_match:
            chat_id = prev_match.group(1)
            curr_page = int(prev_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                "Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        curr_page - 1, CHAT_SETTINGS, "stngs", chat=chat_id)))

        elif next_match:
            chat_id = next_match.group(1)
            next_page = int(next_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                "Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        next_page + 1, CHAT_SETTINGS, "stngs", chat=chat_id)))

        elif back_match:
            chat_id = back_match.group(1)
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                text="Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(escape_markdown(chat.title)),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)))

        # ensure no spinny white circle
        bot.answer_callback_query(query.id)
        query.message.delete()
    except BadRequest as excp:
        if excp.message == "Message is not modified":
            pass
        elif excp.message == "Query_id_invalid":
            pass
        elif excp.message == "Message can't be deleted":
            pass
        else:
            LOGGER.exception("Exception in settings buttons. %s",
                             str(query.data))


@run_async
def get_settings(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]

    # ONLY send settings in PM
    if chat.type != chat.PRIVATE:
        if is_user_admin(chat, user.id):
            text = "Click here to get this chat's settings, as well as yours."
            msg.reply_text(
                text,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        text="Settings",
                        url="t.me/{}?start=stngs_{}".format(
                            context.bot.username, chat.id))
                ]]))
        else:
            text = "Click here to check your settings."

    else:
        send_settings(chat.id, user.id, True)


@run_async
def donate(update: Update, context: CallbackContext):
    user = update.effective_message.from_user
    chat = update.effective_chat  # type: Optional[Chat]
    bot = context.bot
    if chat.type == "private":
        update.effective_message.reply_text(
            DONATE_STRING,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True)

        if OWNER_ID != 254318997 and DONATION_LINK:
            update.effective_message.reply_text(
                "You can also donate to the person currently running me "
                "[here]({})".format(DONATION_LINK),
                parse_mode=ParseMode.MARKDOWN)

    else:
        try:
            bot.send_message(
                user.id,
                DONATE_STRING,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True)

            update.effective_message.reply_text(
                "I've PM'ed you about donating to my creator!")
        except Unauthorized:
            update.effective_message.reply_text(
                "Contact me in PM first to get donation information.")


def migrate_chats(update: Update, context: CallbackContext):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("Migrating from %s, to %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOGGER.info("Successfully migrated!")
    raise DispatcherHandlerStop


def main():

    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.sendMessage(f"@Stuxnet_1_official", "🦋⃟ƓƠƊ ƠƑ ωοℓƒ ✗ 𝄞✿‌᭄ Started! Working Fine For Status, Click /start And /help For More Info[.](https://telegra.ph/file/29abe9f8ef27e254dac35.jpg)", parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                  [                  
                       InlineKeyboardButton(
                             text="Support 🚑",
                             url=f"https://t.me/Stuxnet_1_official"),
                       InlineKeyboardButton(
                             text="Updates 📢",
                             url="https://t.me/stuxnetBotz")
                     ] 
                ]
            ),
        ) 
        except Unauthorized:
            LOGGER.warning(
                "Wolf can't able to send message to support_chat, go and check!")
        except BadRequest as e:
            LOGGER.warning(e.message)


    test_handler = CommandHandler("test", test)
    start_handler = CommandHandler("start", start)

    help_handler = CommandHandler("help", get_help)
    help_callback_handler = CallbackQueryHandler(
        help_button, pattern=r"help_.*")

    settings_handler = CommandHandler("settings", get_settings)
    about_callback_handler = CallbackQueryHandler(Masha_about_callback, pattern=r"masha_")
    source_callback_handler = CallbackQueryHandler(Source_about_callback, pattern=r"source_")
    settings_callback_handler = CallbackQueryHandler(
        settings_button, pattern=r"stngs_")

    donate_handler = CommandHandler("donate", donate)
    migrate_handler = MessageHandler(Filters.status_update.migrate,
                                     migrate_chats)

    # dispatcher.add_handler(test_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(about_callback_handler)
    dispatcher.add_handler(source_callback_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(settings_handler)
    dispatcher.add_handler(help_callback_handler)
    dispatcher.add_handler(settings_callback_handler)
    dispatcher.add_handler(migrate_handler)
    dispatcher.add_handler(donate_handler)

    dispatcher.add_error_handler(error_callback)

    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(
                url=URL + TOKEN, certificate=open(CERT_PATH, 'rb'))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4, clean=True)

    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()

    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)
    pbot.start()
    main()
