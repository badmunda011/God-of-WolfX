import random
import threading
from typing import Union

from MashaRoBot.modules.helper_funcs.msg_types import Types
from MashaRoBot.modules.sql import BASE, SESSION
from sqlalchemy import BigInteger, Boolean, Column, String, UnicodeText

DEFAULT_WELCOME = 'ஏய் {first}, நீங்கள் எப்படி இருக்கிறீர்கள்?'
DEFAULT_GOODBYE = 'பேச தெரிஞ்சா பேசு தேவையில்லாம பேசி அடிவாங்கி சாகதா 🤬!'

DEFAULT_WELCOME_MESSAGES = [
    "{first} is here!",  # Discord welcome messages copied
    "Ready player {first}",
    "Armin, {first} is here.",
    "A wild {first} appeared.",
    "{first} came in like a Lion!",
    "{first} has joined your party.",
    "{first} just joined. Can I get a heal?",
    "{first} just joined the chat - asdgfhak!",
    "{first} just joined. Everyone, look busy!",
    "Welcome, {first}. Stay awhile and listen.",
    "Welcome, {first}. We were expecting you ( ͡° ͜ʖ ͡°)",
    "Welcome, {first}. We hope you brought pizza.",
    "Welcome, {first}. Leave your weapons by the door.",
    "Swoooosh. {first} just landed.",
    "Brace yourselves. {first} just joined the chat.",
    "{first} just joined. Hide your bananas.",
    "{first} just arrived. Seems OP - please nerf.",
    "{first} just slid into the chat.",
    "A {first} has spawned in the chat.",
    "Big {first} showed up!",
    "Where’s {first}? In the chat!",
    "{first} hopped into the chat. Kangaroo!!",
    "{first} just showed up. Hold my beer.",
    "Challenger approaching! {first} has appeared!",
    "It's a bird! It's a plane! Nevermind, it's just {first}.",
    r"It's {first}! Praise the sun! \o/",
    "Never gonna give {first} up. Never gonna let {first} down.",
    "Ha! {first} has joined! You activated my trap card!",
    "Hey! Listen! {first} has joined!",
    "We've been expecting you {first}",
    "It's dangerous to go alone, take {first}!",
    "{first} has joined the chat! It's super effective!",
    "Cheers, love! {first} is here!",
    "{first} is here, as the prophecy foretold.",
    "{first} has arrived. Party's over.",
    "{first} is here to kick butt and chew bubblegum. And {first} is all out of gum.",
    "Hello. Is it {first} you're looking for?",
    "{first} has joined. Stay awhile and listen!",
    "Roses are red, violets are blue, {first} joined this chat with you",
    "Welcome {first}, Avoid Punches if you can!",
    "It's a bird! It's a plane! - Nope, its {first}!",
    "{first} Joined! - Ok.",  # Discord welcome messages end.
    "All Hail {first}!",
    "Hi, {first}. Don't lurk, only Titans do that.",
    "{first} has joined the battle bus.",
    "A new Challenger enters!",  # Tekken
    "Ok!",
    "{first} just fell into the chat!",
    "Something just fell from the sky! - oh, its {first}.",
    "{first} Just teleported into the chat!",
    "Hi, {first}, show me your Hunter License!",  # Hunter Hunter
    "I'm looking for Levi, oh wait nvm it's {first}.",  # One Punch man s2
    "Welcome {first}, leaving is not an option!",
    "Run Forest! ..I mean...{first}.",
    "Huh?\nDid someone with a Disaster level just join?\nOh wait, it's just {first}.",  # One Punch ma
    "Hey, {first}, ever heard the Titan Engine?",  # One Punch ma
    "Hey, {first}, empty your pockets.",
    "Hey, {first}!, are you strong?",
    "Call the Avengers! - {first} just joined the chat.",
    "{first} joined. You must construct additional pylons.",
    "Ermagherd. {first} is here.",
    "Come for the Snail Racing, Stay for the Chimichangas!",
    "Who needs Google? You're everything we were searching for.",
    "This place must have free WiFi, cause I'm feeling a connection.",
    "Speak friend and enter.",
    "Welcome you are",
    "Welcome {first}, your princess is in another castle.",
    "Hi {first}, welcome to the dark side.",
    "Hola {first}, beware of people with disaster levels",
    "Hey {first}, we have the droids you are looking for.",
    "Hi {first}\nThis isn't a strange place, this is my home, it's the people who are strange.",
    "Oh, hey {first} what's the password?",
    "Hey {first}, I know what we're gonna do today",
    "{first} just joined, be at alert they could be a spy.",
    "{first} joined the group, read by Mark Zuckerberg, CIA and 35 others.",
    "Welcome {first}, watch out for falling monkeys.",
    "Everyone stop what you’re doing, We are now in the presence of {first}.",
    "Hey {first}, do you wanna know how I got these scars?",
    "Welcome {first}, drop your weapons and proceed to the spy scanner.",
    "Stay safe {first}, Keep 3 meters social distances between your messages.",  # Corona memes lmao
    "Hey {first}, Do you know I once One-punched a meteorite?",
    "You’re here now {first}, Resistance is futile",
    "{first} just arrived, the force is strong with this one.",
    "{first} just joined on president’s orders.",
    "Hi {first}, is the glass half full or half empty?",
    "Yipee Kayaye {first} arrived.",
    "Welcome {first}, if you’re a secret agent press 1, otherwise start a conversation",
    "{first}, I have a feeling we’re not in Kansas anymore.",
    "They may take our lives, but they’ll never take our {first}.",
    "Coast is clear! You can come out guys, it’s just {first}.",
    "Welcome {first}, pay no attention to that guy lurking.",
    "Welcome {first}, may the force be with you.",
    "May the {first} be with you.",
    "{first} just joined. Hey, where's Perry?",
    "{first} just joined. Oh, there you are, Perry.",
    "Ladies and gentlemen, I give you ...  {first}.",
    "Behold my new evil scheme, the {first}-Inator.",
    "Ah, {first} the Platypus, you're just in time... to be trapped.",
    "{first} just arrived. Diable Jamble!",  # One Piece Sanji
    "{first} just arrived. Aschente!",  # No Game No Life
    "{first} say Aschente to swear by the pledges.",  # No Game No Life
    "{first} just joined. El Psy congroo!",  # Steins Gate
    "Irasshaimase {first}!",  # weeabo shit
    "Hi {first}, what is 1000-7?",  # tokyo ghoul
    "Come. I don't want to destroy this place",  # hunter x hunter
    "I... am... Whitebeard!...wait..wrong anime.",  # one Piece
    "Hey {first}...have you ever heard these words?",  # BNHA
    "Can't a guy get a little sleep around here?",  # Kamina Falls – Gurren Lagann
    "It's time someone put you in your place, {first}.",  # Hellsing
    "Unit-01's reactivated..",  # Neon Genesis: Evangelion
    "Prepare for trouble...And make it double",  # Pokemon
    "Hey {first}, are You Challenging Me?",  # Shaggy
    "Oh? You're Approaching Me?",  # jojo
    "Ho… mukatta kuruno ka?",  # jojo jap ver
    "I can't beat the shit out of you without getting closer",  # jojo
    "Ho ho! Then come as close as you'd like.",  # jojo
    "Hoho! Dewa juubun chikazukanai youi",  # jojo jap ver
    "Guess who survived his time in Hell, {first}.",  # jojo
    "How many loaves of bread have you eaten in your lifetime?",  # jojo
    "What did you say? Depending on your answer, I may have to kick your ass!",  # jojo
    "Oh? You're approaching me? Instead of running away, you come right to me? Even though your grandfather, Joseph, told you the secret of The World, like an exam student scrambling to finish the problems on an exam until the last moments before the chime?",  # jojo
    "Rerorerorerorerorero.",  # jojo
    "{first} just warped into the group!",
    "I..it's..it's just {first}.",
    "Sugoi, Dekai. {first} Joined!",
    "{first}, do you know gods of death love apples?",  # Death Note owo
    "I'll take a potato chip.... and eat it",  # Death Note owo
    "Oshiete oshiete yo sono shikumi wo!",  # Tokyo Ghoul
    "Kaizoku ou ni...nvm wrong anime.",  # op
    "{first} just joined! Gear.....second!",  # Op
    "Omae wa mou....shindeiru",
    "Hey {first}, the leaf village lotus blooms twice!",  # Naruto stuff begins from here
    "{first} Joined! Omote renge!",
    "{first}! I, Madara! declare you the strongest",
    "{first}, this time I'll lend you my power. ",  # Kyuubi to naruto
    "{first}, welcome to the hidden leaf village!",  # Naruto thingies end here
    "In the jungle, you must wait...until the dice read five or eight.",  # Jumanji stuff
    "Dr.{first} Famed archeologist and international explorer,\nWelcome to Jumanji!\nJumanji's Fate is up to you now.",
    "{first}, this will not be an easy mission - monkeys slow the expedition.",  # End of Jumanji stuff
    "Remember, remember, the Fifth of November, the Gunpowder Treason and Plot. I know of no reason why the Gunpowder Treason should ever be forgot.", #V for Vendetta
    "The only verdict is vengeance; a vendetta, held as a votive not in vain, for the value and veracity of such shall one day vindicate the vigilant and the virtuous.", #V for Vendetta
    "Behind {first} there is more than just flesh. Beneath this user there is an idea... and ideas are bulletproof.", #V for Vendetta
    "Love your rage, not your cage.", #V for Vendetta
    "Get your stinking paws off me, you damned dirty ape!", #Planet of the apes
    "Elementary, my dear {first}.",
    "I'm back - {first}.",
    "Bond. {first} Bond.",
    "Come with me if you want to live",
    "I Believe My Squad Will Be Victorious! ...",
    "You Have The Freedom To Defend The World's Freedom And I Have The Freedom To Continue Moving Forward.",
    "I'm The Same As You {first},I didnt had any choice",
    "I'm Not Planning On Handing It Down To Any Of You",
    "I'm Gonna Destroy Them! Every last one of those titans thats on this earth",
    "Hey {first} If we kill all our enemies over there will we finally be free?",
    "You're Not a Soldier {first}",
    " Sasageyo, Sasageyo! {first}wa Sasageyo",
]
DEFAULT_GOODBYE_MESSAGES = [
    "ஏன் என்னை பிரிந்தாய் என் உயிரே என் உயிரே🥺💔.",
    "தனியாக தவிக்கின்றேன் துணைவேண்டாம் அன்பே போ🥺.",
    "மறந்தாயே மறந்தாயே பெண்ணே என்னை ஏன் மறந்தாய் கடந்தேதான் நடந்தாயே யாரோ என்று ஏன் கடந்தாய்!🥺💔.",
    "{first} has left the clan.",
    "{first} has left the game.",
    "பேச தெரிஞ்சா பேசு தேவையில்லாம பேசி அடிவாங்கி சாகதா 🤬.",
    "மனசார சொல்றேன் டா சாத்தியமா நீ எல்லாம் உருப்பட மாட்ட உருப்படவே மாட்ட🤦‍♀",
    "அய்யயோ! இந்த ஆளு Teacher-அ வச்சுருக்கான்டோ அதை நான் பாத்து போட்டேன்டோ😆",
    "போட எச்ச பயலே 🥶💦.",
    "We hope to see you again soon, {first}.",
    "ஏன்டா அறிவுகெட்டவனே அறிவு இருக்கா உனக்கு மடப்பயலே முட்டா பயலே சோத்தை திங்கிறியா இல்ல சோத்தை விட்டுட்டு லட்டியை திங்கிறியா டா😂😂🤣🤣.",
    "ஜிஞ்சர் ஈட்டிங்க் மங்க்கி 🐵",
    "அடேய் பொறம்போக்கு வீட்ல சொல்லிட்டு வந்தியா ?.",
    "Please don't leave me alone in this place, {first}!",
    "அடிவாங்குறதுக்குனே அளவெடுத்து செஞ்சமாதிரி இருக்கான்👊",
    "என்னப்பா உனக்கு பிரச்சன? 😣",
    "ஆணியே புடுங்க வேணாம்🙄.",
    "யார் எடத்துல வந்து  யார் Scene-அ போடுறது  செஞ்சுருவேன்😤😡.",
    "மூடிட்டு போடா வெண்ண! 😂.",
    "நீ பெரிய முட்டாள்னு எனக்கு எப்பயோ தெரியும்! 😜",
    "மனசார சொல்றேன் டா சாத்தியமா நீ எல்லாம் உருப்பட மாட்ட உருப்படவே மாட்ட🤦‍♀",
    "போ நீ போ 🚶‍♂",
    "ஏண்டா நாயா அடிக்கிற நாயே🐶",
    "டேய் நீ நல்லா இருக்க மாட்டடா நல்லாவே இருக்க மாட்டடா நாசமா போனவன்😑🤧",
    "இது எல்லாம் ஒரு பொழப்பு 🥵 போய் பிச்சை எடு போ",
    "அடிங்கு ஓடி போ நாயே! 🐕",
    "அடப்பாவி சண்டாளா நீயா டா என்னை கலாய்க்க வந்த🤧",
    "அடப்பாவி சண்டாளா நீயா டா என்னை கலாய்க்க வந்த🤧",
    "ஏன்டா அறிவுகெட்டவனே அறிவு இருக்கா உனக்கு மடப்பயலே முட்டா பயலே சோத்தை திங்கிறியா இல்ல சோத்தை விட்டுட்டு லட்டியை திங்கிறியா டா😂😂🤣🤣",
    "ஏன்டா அறிவுகெட்டவனே அறிவு இருக்கா உனக்கு மடப்பயலே முட்டா பயலே சோத்தை திங்கிறியா இல்ல சோத்தை விட்டுட்டு லட்டியை திங்கிறியா டா😂😂🤣🤣",
    "ஏண்டா நாயா அடிக்கிற நாயே🐶",
    "என்னப்பா உனக்கு பிரச்சன? 😣",
    "டேய் இந்த எகத்தாலமெல்லாம் என்கிட்டே வெச்சிக்காதா",
    "வாய்ப்பில்ல ராஜா.",
    "மூடிட்டு போடா வெண்ண! 😂",
    "போடா 🦊 நரி",
    "டேய் எனக்கு வெறி வர்றதுக்குள்ள இங்கிருந்து போய்டுடா😡",
    "ரத்தம் கக்கி சாவு 🙊",
    "என்ன Look-உ அப்படியே கண்ண புடுங்கி தின்னுபுடுவேன் மொகரைய பாரு மொகரைய என்ன என்னாடா என்னா😏.",
    "டேய் டேய் மூஞ்சியும் மொகரையும் பாரு🤯",
    "நல்லவர்களை நம்புங்கள்",
    "இறப்பதற்கு வாழ்க.",
    "இஞ்சி தின்ன கொரங்கு மாறி இருக்க 🐵",
    "பொண்ண பெக்க சொன்னா பொறுக்கிய பெத்துவிட்டுருக்காய்ங்க!😂😒",
    "அடிங்கு ஓடி போ நாயே! 🐕",
    "பிசாசுக்கு பொறந்த பிசாசே👻",
    "மூடிட்டு போடா வெண்ண! 😂",
    "அறிவு கெட்ட நாதாரி😤",
    "டேய் எனக்கு வெறி வர்றதுக்குள்ள இங்கிருந்து போய்டுடா😡",
    "பன்னிக்குட்டி எல்லாம் பஞ்சு டயலாக் பேசுதடா🤯",
    "நீ மங்குனி அமைச்சர் என்பதை மணிக்கு ஒருமுறை நிரூபித்துக் கொண்டே இருக்கிறாய்! 😂",
    "ஒரு பாவி மட்டுமே",
    "சென்று வாருங்கள்🥰",
    "நீங்கள் பார்த்த பிரச்சனைகள் யாருக்கும் தெரியாது",
    "மௌனமான மரணம் ஒன்று உயிரை கொண்டு போனதே உயரமான கனவு இன்று தரையில் வீழ்ந்து போனதே💔",
    "நீங்கள் திரும்ப வந்தால் மீண்டும் வரவேற்க காத்திருப்பேன்🥳",
    "சென்று வாருங்கள்🥰",
    "வெளிய போங்கடா அயோக்கிய ராஸ்கல்களா!😏",
    "வெளியே செல்",
    "கனவே கனவே கலைவதேனோ கணங்கள் ரணமாய் கரைவதேனோ நினைவே நினைவே அரைவதேனோ எனது உலகம் உடைவதேனோ💔",
] 
# Line 111 to 152 are references from https://bindingofisaac.fandom.com/wiki/Fortune_Telling_Machine


class Welcome(BASE):
    __tablename__ = "welcome_pref"
    chat_id = Column(String(14), primary_key=True)
    should_welcome = Column(Boolean, default=True)
    should_goodbye = Column(Boolean, default=True)
    custom_content = Column(UnicodeText, default=None)

    custom_welcome = Column(
        UnicodeText, default=random.choice(DEFAULT_WELCOME_MESSAGES)
    )
    welcome_type = Column(BigInteger, default=Types.TEXT.value)

    custom_leave = Column(UnicodeText, default=random.choice(DEFAULT_GOODBYE_MESSAGES))
    leave_type = Column(BigInteger, default=Types.TEXT.value)

    clean_welcome = Column(BigInteger)

    def __init__(self, chat_id, should_welcome=True, should_goodbye=True):
        self.chat_id = chat_id
        self.should_welcome = should_welcome
        self.should_goodbye = should_goodbye

    def __repr__(self):
        return "<Chat {} should Welcome new users: {}>".format(
            self.chat_id, self.should_welcome
        )


class WelcomeButtons(BASE):
    __tablename__ = "welcome_urls"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText, nullable=False)
    url = Column(UnicodeText, nullable=False)
    same_line = Column(Boolean, default=False)

    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = str(chat_id)
        self.name = name
        self.url = url
        self.same_line = same_line


class GoodbyeButtons(BASE):
    __tablename__ = "leave_urls"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText, nullable=False)
    url = Column(UnicodeText, nullable=False)
    same_line = Column(Boolean, default=False)

    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = str(chat_id)
        self.name = name
        self.url = url
        self.same_line = same_line


class WelcomeMute(BASE):
    __tablename__ = "welcome_mutes"
    chat_id = Column(String(14), primary_key=True)
    welcomemutes = Column(UnicodeText, default=False)

    def __init__(self, chat_id, welcomemutes):
        self.chat_id = str(chat_id)  # ensure string
        self.welcomemutes = welcomemutes


class WelcomeMuteUsers(BASE):
    __tablename__ = "human_checks"
    user_id = Column(BigInteger, primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    human_check = Column(Boolean)

    def __init__(self, user_id, chat_id, human_check):
        self.user_id = user_id  # ensure string
        self.chat_id = str(chat_id)
        self.human_check = human_check


class CleanServiceSetting(BASE):
    __tablename__ = "clean_service"
    chat_id = Column(String(14), primary_key=True)
    clean_service = Column(Boolean, default=True)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)

    def __repr__(self):
        return "<Chat used clean service ({})>".format(self.chat_id)


Welcome.__table__.create(checkfirst=True)
WelcomeButtons.__table__.create(checkfirst=True)
GoodbyeButtons.__table__.create(checkfirst=True)
WelcomeMute.__table__.create(checkfirst=True)
WelcomeMuteUsers.__table__.create(checkfirst=True)
CleanServiceSetting.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()
WELC_BTN_LOCK = threading.RLock()
LEAVE_BTN_LOCK = threading.RLock()
WM_LOCK = threading.RLock()
CS_LOCK = threading.RLock()


def welcome_mutes(chat_id):
    try:
        welcomemutes = SESSION.query(WelcomeMute).get(str(chat_id))
        if welcomemutes:
            return welcomemutes.welcomemutes
        return False
    finally:
        SESSION.close()


def set_welcome_mutes(chat_id, welcomemutes):
    with WM_LOCK:
        prev = SESSION.query(WelcomeMute).get((str(chat_id)))
        if prev:
            SESSION.delete(prev)
        welcome_m = WelcomeMute(str(chat_id), welcomemutes)
        SESSION.add(welcome_m)
        SESSION.commit()


def set_human_checks(user_id, chat_id):
    with INSERTION_LOCK:
        human_check = SESSION.query(WelcomeMuteUsers).get((user_id, str(chat_id)))
        if not human_check:
            human_check = WelcomeMuteUsers(user_id, str(chat_id), True)

        else:
            human_check.human_check = True

        SESSION.add(human_check)
        SESSION.commit()

        return human_check


def get_human_checks(user_id, chat_id):
    try:
        human_check = SESSION.query(WelcomeMuteUsers).get((user_id, str(chat_id)))
        if not human_check:
            return None
        human_check = human_check.human_check
        return human_check
    finally:
        SESSION.close()


def get_welc_mutes_pref(chat_id):
    welcomemutes = SESSION.query(WelcomeMute).get(str(chat_id))
    SESSION.close()

    if welcomemutes:
        return welcomemutes.welcomemutes

    return False


def get_welc_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()
    if welc:
        return (
            welc.should_welcome,
            welc.custom_welcome,
            welc.custom_content,
            welc.welcome_type,
        )

    else:
        # Welcome by default.
        return True, DEFAULT_WELCOME, None, Types.TEXT


def get_gdbye_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()
    if welc:
        return welc.should_goodbye, welc.custom_leave, welc.leave_type
    else:
        # Welcome by default.
        return True, DEFAULT_GOODBYE, Types.TEXT


def set_clean_welcome(chat_id, clean_welcome):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id))

        curr.clean_welcome = int(clean_welcome)

        SESSION.add(curr)
        SESSION.commit()


def get_clean_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()

    if welc:
        return welc.clean_welcome

    return False


def set_welc_preference(chat_id, should_welcome):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id), should_welcome=should_welcome)
        else:
            curr.should_welcome = should_welcome

        SESSION.add(curr)
        SESSION.commit()


def set_gdbye_preference(chat_id, should_goodbye):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id), should_goodbye=should_goodbye)
        else:
            curr.should_goodbye = should_goodbye

        SESSION.add(curr)
        SESSION.commit()


def set_custom_welcome(
    chat_id, custom_content, custom_welcome, welcome_type, buttons=None
):
    if buttons is None:
        buttons = []

    with INSERTION_LOCK:
        welcome_settings = SESSION.query(Welcome).get(str(chat_id))
        if not welcome_settings:
            welcome_settings = Welcome(str(chat_id), True)

        if custom_welcome or custom_content:
            welcome_settings.custom_content = custom_content
            welcome_settings.custom_welcome = custom_welcome
            welcome_settings.welcome_type = welcome_type.value

        else:
            welcome_settings.custom_welcome = DEFAULT_WELCOME
            welcome_settings.welcome_type = Types.TEXT.value

        SESSION.add(welcome_settings)

        with WELC_BTN_LOCK:
            prev_buttons = (
                SESSION.query(WelcomeButtons)
                .filter(WelcomeButtons.chat_id == str(chat_id))
                .all()
            )
            for btn in prev_buttons:
                SESSION.delete(btn)

            for b_name, url, same_line in buttons:
                button = WelcomeButtons(chat_id, b_name, url, same_line)
                SESSION.add(button)

        SESSION.commit()


def get_custom_welcome(chat_id):
    welcome_settings = SESSION.query(Welcome).get(str(chat_id))
    ret = DEFAULT_WELCOME
    if welcome_settings and welcome_settings.custom_welcome:
        ret = welcome_settings.custom_welcome

    SESSION.close()
    return ret


def set_custom_gdbye(chat_id, custom_goodbye, goodbye_type, buttons=None):
    if buttons is None:
        buttons = []

    with INSERTION_LOCK:
        welcome_settings = SESSION.query(Welcome).get(str(chat_id))
        if not welcome_settings:
            welcome_settings = Welcome(str(chat_id), True)

        if custom_goodbye:
            welcome_settings.custom_leave = custom_goodbye
            welcome_settings.leave_type = goodbye_type.value

        else:
            welcome_settings.custom_leave = DEFAULT_GOODBYE
            welcome_settings.leave_type = Types.TEXT.value

        SESSION.add(welcome_settings)

        with LEAVE_BTN_LOCK:
            prev_buttons = (
                SESSION.query(GoodbyeButtons)
                .filter(GoodbyeButtons.chat_id == str(chat_id))
                .all()
            )
            for btn in prev_buttons:
                SESSION.delete(btn)

            for b_name, url, same_line in buttons:
                button = GoodbyeButtons(chat_id, b_name, url, same_line)
                SESSION.add(button)

        SESSION.commit()


def get_custom_gdbye(chat_id):
    welcome_settings = SESSION.query(Welcome).get(str(chat_id))
    ret = DEFAULT_GOODBYE
    if welcome_settings and welcome_settings.custom_leave:
        ret = welcome_settings.custom_leave

    SESSION.close()
    return ret


def get_welc_buttons(chat_id):
    try:
        return (
            SESSION.query(WelcomeButtons)
            .filter(WelcomeButtons.chat_id == str(chat_id))
            .order_by(WelcomeButtons.id)
            .all()
        )
    finally:
        SESSION.close()


def get_gdbye_buttons(chat_id):
    try:
        return (
            SESSION.query(GoodbyeButtons)
            .filter(GoodbyeButtons.chat_id == str(chat_id))
            .order_by(GoodbyeButtons.id)
            .all()
        )
    finally:
        SESSION.close()


def clean_service(chat_id: Union[str, int]) -> bool:
    try:
        chat_setting = SESSION.query(CleanServiceSetting).get(str(chat_id))
        if chat_setting:
            return chat_setting.clean_service
        return False
    finally:
        SESSION.close()


def set_clean_service(chat_id: Union[int, str], setting: bool):
    with CS_LOCK:
        chat_setting = SESSION.query(CleanServiceSetting).get(str(chat_id))
        if not chat_setting:
            chat_setting = CleanServiceSetting(chat_id)

        chat_setting.clean_service = setting
        SESSION.add(chat_setting)
        SESSION.commit()


def migrate_chat(old_chat_id, new_chat_id):
    with INSERTION_LOCK:
        chat = SESSION.query(Welcome).get(str(old_chat_id))
        if chat:
            chat.chat_id = str(new_chat_id)

        with WELC_BTN_LOCK:
            chat_buttons = (
                SESSION.query(WelcomeButtons)
                .filter(WelcomeButtons.chat_id == str(old_chat_id))
                .all()
            )
            for btn in chat_buttons:
                btn.chat_id = str(new_chat_id)

        with LEAVE_BTN_LOCK:
            chat_buttons = (
                SESSION.query(GoodbyeButtons)
                .filter(GoodbyeButtons.chat_id == str(old_chat_id))
                .all()
            )
            for btn in chat_buttons:
                btn.chat_id = str(new_chat_id)

        SESSION.commit()
