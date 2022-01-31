from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import config
from db_api import DataBaseHandler

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
admin = config.admin
dp = Dispatcher(bot)
db = DataBaseHandler("history.db")
imdb_token = config.imdb_token

