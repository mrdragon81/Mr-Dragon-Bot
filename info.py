import re
from os import environ
from Script import script

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Main
SESSION = environ.get("SESSION", "Media_search")
API_ID = int(environ.get("API_ID", "26045039"))
API_HASH = environ.get("API_HASH", "affd39f67da102a83f0f9e5c96cf84fe")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
PORT = environ.get("PORT", "8082")

# Owners
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get("ADMINS", "8141314253 ").split()
]
OWNER_USERNAME = environ.get(
    "OWNER_USERNAME", "@MEEDRAGONBOT"
)  # without @ or https://t.me/
USERNAME = environ.get("USERNAME", "@MEEDRAGONBOT")  # ADMIN USERNAME

# Database Channel
CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in environ.get("CHANNELS", "-1002542788675").split()
]

# ForceSub Channel & Log Channels
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002868802089"))
AUTH_REQ_CHANNEL = int(environ.get("AUTH_REQ_CHANNEL", "-1002868802089"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002988640125"))
LOG_API_CHANNEL = int(environ.get("LOG_API_CHANNEL", "-1002988640125"))
LOG_VR_CHANNEL = int(environ.get("LOG_VR_CHANNEL", "-1002988640125"))

# MongoDB
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://mrdragon82:mrdragon82@cluster0.25cqmdm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")

# Files index database url
FILES_DATABASE = environ.get("FILES_DATABASE", "mongodb+srv://mrdragon:mrdragon@cluster0.ebdcfhn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "jisshu")

# Other Channel's
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1003019479337"))
DELETE_CHANNELS = int(environ.get("DELETE_CHANNELS", "-1002988640125"))
request_channel = environ.get("REQUEST_CHANNEL", "-1002800325917")
REQUEST_CHANNEL = (
    int(request_channel)
    if request_channel and id_pattern.search(request_channel)
    else None
)
MOVIE_UPDATE_CHANNEL = int(environ.get("MOVIE_UPDATE_CHANNEL", "-1002868802089"))

# Added Link Here Not Id
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "https://t.me/+s5et_Xgzy0w4NTA1")
MOVIE_GROUP_LINK = environ.get("MOVIE_GROUP_LINK", "https://t.me/KarnatakaKingmovies")

# Verification
IS_VERIFY = is_enabled("IS_VERIFY", True)
# ---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/+DLC4ztUnnVdmYzY1")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/+DLC4ztUnnVdmYzY1")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/+DLC4ztUnnVdmYzY1")
VERIFY_IMG = environ.get(
    "VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg"
)
SHORTENER_API = environ.get("SHORTENER_API", "b460d2482ff023d8ce65e20415c7994ea8d68ae0")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shortxlinks.com")
SHORTENER_API2 = environ.get(
    "SHORTENER_API2", "b460d2482ff023d8ce65e20415c7994ea8d68ae0"
)
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "shortxlinks.com")
SHORTENER_API3 = environ.get(
    "SHORTENER_API3", "b460d2482ff023d8ce65e20415c7994ea8d68ae0"
)
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "shortxlinks.com")
TWO_VERIFY_GAP = int(environ.get("TWO_VERIFY_GAP", "1800"))
THREE_VERIFY_GAP = int(environ.get("THREE_VERIFY_GAP", "1800"))

# Language & Quality & Season & Year
LANGUAGES = [
    "hindi",
    "english",
    "telugu",
    "tamil",
    "kannada",
    "malayalam",
    "bengali",
    "marathi",
    "gujarati",
    "punjabi",
    "marathi",
]
QUALITIES = [
    "HdRip",
    "web-dl",
    "bluray",
    "hdr",
    "fhd",
    "240p",
    "360p",
    "480p",
    "540p",
    "720p",
    "960p",
    "1080p",
    "1440p",
    "2K",
    "2160p",
    "4k",
    "5K",
    "8K",
]
YEARS = [f"{i}" for i in range(2025, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]

# Pictures And Reaction
START_IMG = (💯😊
    environ.get(
        "START_IMG"💯,
        "https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg",
    )
).split()
FORCESUB_IMG = environ.get("FORCESUB_IMG", "https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg")
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split()
PAYPICS = (https://graph.org/file/efa2fe61633bbf798e66e-08eb6809d50ae3bf7b.jpg
    environ.get("PAYPICS", "https://graph.org/file/9f3f47c690bbcc67633c2.jpg")
).split()
SUBSCRIPTION = environ.get(
    "SUBSCRIPTION", "https://graph.org/file/9f3f47c690bbcc67633c2.jpg"
)
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]


# Other Funtions
FILE_AUTO_DEL_TIMER = int(environ.get("FILE_AUTO_DEL_TIMER", "600"))
AUTO_FILTER = is_enabled("AUTO_FILTER", True)
IS_PM_SEARCH = is_enabled("IS_PM_SEARCH", True)
IS_SEND_MOVIE_UPDATE = is_enabled(
    "IS_SEND_MOVIE_UPDATE", False
)  # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
MAX_BTN = int(environ.get("MAX_BTN", "8"))
AUTO_DELETE = is_enabled("AUTO_DELETE", True)
DELETE_TIME = int(environ.get("DELETE_TIME", 300))
IMDB = is_enabled("IMDB", False)
FILE_CAPTION = environ.get("FILE_CAPTION", f"{script.FILE_CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
PROTECT_CONTENT = is_enabled("PROTECT_CONTENT", False)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
LINK_MODE = is_enabled("LINK_MODE", True)
TMDB_API_KEY = environ.get("TMDB_API_KEY", "")

# Online Streaming And Download
STREAM_MODE = bool(environ.get("STREAM_MODE", True))  # Set True or Flase

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if "DYNO" in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "")

# Commands
admin_cmds = [
    "/add_premium - Add A User To Premium",
    "/premium_users - View All Premium Users",
    "/remove_premium - Remove A User's Premium Status",
    "/add_redeem - Generate A Redeem Code",
    "/refresh - Refresh Free Trail",
    "/set_muc - Set Movie Update Channel",
    "/pm_search_on - Enable PM Search",
    "/pm_search_off - Disable PM Search",
    "/set_ads - Set Advertisements",
    "/del_ads - Delete Advertisements",
    "/setlist - Set Top Trending List",
    "/clearlist - Clear Top Trending List",
    "/verify_id - Verification Off ID",
    "/index - Index Files",
    "/send - Send Message To A User",
    "/leave - Leave A Group Or Channel",
    "/ban - Ban A User",
    "/unban - Unban A User",
    "/broadcast - Broadcast Message",
    "/grp_broadcast - Broadcast Messages To Groups",
    "/delreq - Delete Join Request",
    "/channel - List Of Database Channels",
    "/del_file - Delete A Specific File",
    "/delete - Delete A File(By Reply)",
    "/deletefiles - Delete Multiple Files",
    "/deleteall - Delete All Files",
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Currunt Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"},
]
