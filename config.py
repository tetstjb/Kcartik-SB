import logging
from telethon import TelegramClient
from os import getenv
from strings.helpers import DEV
from dotenv import load_dotenv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
BOT_TOKEN = getenv("BOT_TOKEN", default=7439465700:AAHpUg8hRiUmc58LHlKU5MT2L60IYjo0Ywc)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=7057311155:AAG_Dlx5XWNsJHfSkzC80wPsGgUphPnUC9c)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=7283556606:AAFfzGlQ2P6vVaM77qjILEhoeEiENCQowRQ)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=6943426838:AAHbWOFJXVmqF4dOfsoBI0UcMGivS4qSAV8)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=7233522808:AAGJGcSfNopU37TcCBL17kvgFW5gPx3El1U)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=7280498981:AAHmzA3det7GRFsGzg19O_UBIoKTbVmj_Lw)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=7280078504:AAF85twIv6wDnEtnzi6nqM1HLiveLgr1kv8)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=6967383365:AAE5uqpGWq_nWhF7-WdX8hzz3KWB7UMPuqs)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=6371312644:AAGMpLgUh4rkV9OBCuav1QzxLhG2J6p5CHc)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=7314911417:AAGnRufpMFuhTEWPq4nZCtMG66TxvNsJedM)

SUDO_USERS = getenv("SUDO_USERS", "7353019847 1363590620 6829314029 7067480930 5960968099 6692315925 1170067159 7067480930 7058553951 1402043827").split()

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7353019847 1363590620 6829314029 7067480930 5960968099 6692315925 1170067159 7067480930 7058553951 1402043827").split()))
for x in DEV:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7345260405"))
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
