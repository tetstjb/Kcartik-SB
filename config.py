import logging
from telethon import TelegramClient
from os import getenv
from strings.helpers import DEV
from dotenv import load_dotenv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

API_ID = 25497009
API_HASH = "493de7f9056f1c4e979b963357fa1dad"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
BOT_TOKEN = getenv("7667058722:AAGs3-aJDynd2X4lXiD3_Kl8QLSdeWQENfM", default=None)
BOT_TOKEN2 = getenv("7204544367:AAEMALkSSm-WXSzi4AhyWCj2YXC4EPSVsis", default=None)
BOT_TOKEN3 = getenv("7374596497:AAFGiL9mLO5nuHaAPPZTfTm7fy23NgnulSc", default=None)
BOT_TOKEN4 = getenv("7565881558:AAF1VR2ymocLFmOsquKp0LS4L3JaVxfv_qc", default=None)
BOT_TOKEN5 = getenv("7988992893:AAEJBohYeV5hJuBdFC_R6Yga7xO-o8Ji8QI", default=None)
BOT_TOKEN6 = getenv("7553515643:AAEN5CRZjUqxqkI_JJN7dkRfVg1CQWxx1mI", default=None)
BOT_TOKEN7 = getenv("7629992402:AAFMuuCeoYlBrKN_aYD8-VVeAT1rgCO_wQs", default=None)
BOT_TOKEN8 = getenv("7602909659:AAHT3P8SdMd3Pjt8RhGYokS-vEYIomBPMcQ", default=None)
BOT_TOKEN9 = getenv("7995024819:AAGZSTIDG7FyYSjUNiy9lVlXtVQRyntmf1I", default=None)
BOT_TOKEN10 = getenv("7664789386:AAG2vSE0l9g4o35GFrs8bYad7W3IYRc3la8", default=None)

SUDO_USERS = getenv("SUDO_USERS", "7196352887 1210740296 8190864926 7695694711 6053231890 5344438159 6686762409").split()

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7196352887 1210740296 8190864926 7695694711 6053231890 5344438159 6686762409").split()))
for x in DEV:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7695694711"))
SUDO_USERS.append(OWNER_ID)

KEX1 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
KEX2 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
KEX3 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
KEX4 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
KEX5 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
KEX6 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
KEX7 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
KEX8 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
KEX9 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
KEX10 = TelegramClient('ꜱ ᴛ ᴏ ʀ ᴍ 10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
