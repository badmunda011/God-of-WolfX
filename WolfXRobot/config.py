import json
import os


def get_user_list(config, key):
    with open('{}/WolfXRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
  
    TEMP_DOWNLOAD_DIRECTORY = 'None'
    ARQ_API = 'BJWJFF-ABOVMF-IPHAEN-QHXPTJ-ARQ'
    ARQ_API_URL = 'arq.hamker.in'
    API_ID = '8967766'
    API_HASH = '505dc1f394f59c8a55b1aa798a0715f9'
    TOKEN = '2079359720:AAFO_39OA9oAuy5UoX67OXduzBBw1eyeOoE'
    OWNER_ID = 960432019
    OWNER_USERNAME = "BavaBee"
    SUPPORT_CHAT = 'HangOverXD'
    JOIN_LOGGER = -1001648239341
    EVENT_LOGS = -1001648239341
    REM_BG_API_KEY = "dxsh728mZMDmj4ijSZCNPZig"
    STRING_SESSION = "1BVtsOH4Bu2v0wASaMCuV0PgHpopdRrfpm3-q4WHj02C_LbCv_I-5Yz9dCmEocnXAdv3cvJL9sas4ZCU_mmOD2xxzT4VETq5K--e1CNfypg-9IhWEB-wr581BVC73lQic7hKvbfWOwBDRH12fBSmf3shLEBYXiw2JJ6QWolRg1co-8VawR2gCk0gu1C6Q0NCyg0JN2pkV3Vmgi1fghIT3cjSQ9q85qdXEsAPAdILyQ9IexUsKwxvuykOOh7jwpAc_HPanZh8908bZi_sKh-sdh4ywaHMwfTahHQi5oF2EE6eBQ-QzjfG49kBMi4BJNoRGgZCGMt4lIYeMsa5gu5rX9QpcD3TLGV0="
    ALLOW_CHATS = "True"
    SQLALCHEMY_DATABASE_URI = 'postgres://ifdgcebj:NW_PMVUxlDscvmZO5yKu3kEQgI013JLg@castor.db.elephantsql.com/ifdgcebj'  
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_ID = "2079359720"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'awoo'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
