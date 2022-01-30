import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from data import config
from handlers.dbhandler import DataBaseHandler
from handlers.imdb_handler import search_by_expression_imdb


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
admins = config.admins
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = DataBaseHandler("history.db")
imdb_token = config.imdb_token


# TODO:
#  - Code-architecture lol
#  - Deploy on AWS
#  - Add inline0-buttons
#  - Cover bot with unit-tests
#  - Add support of kinopoisk
#  - Add distinguishing between languages to select API (only for russian: kinopoisk.ru)
#  - Add fetching online video services by request
#  - Add fetching of random movie-title and information about ("I don't know what to watch!")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    greet_photo = "https://sun9-24.userapi.com/impg/cxB56z6cKXnOuhHq4kS_vomHW1OyvPKfrhoFfw/HhdCGnmWIV0.jpg?size=640x480&quality=96&sign=5f84ecb9a62e7fc3e0037de637a20379&type=album"
    await bot.send_photo(
        message.from_user.id,
        photo=greet_photo
    )
    await message.reply(f"Привет, {message.from_user.full_name}!\nЯ умею обрабатывать запросы о фильмах!")


@dp.message_handler(commands=["help"])
async def helper(message: types.Message):
    await message.reply("Привет! \nЭто хелпер для помощи в отладке!")


@dp.message_handler(commands=["my_id"])
async def get_user_id(message: types.Message):
    await bot.send_message(message.from_user.id, message.from_user.id)


@dp.message_handler()
async def movie_handler(message: types.Message):
    logging.info(F"message - {message.text} from {message.from_user.id}")
    users_request = message.text
    print('58')
    imdb_data = await search_by_expression_imdb(imdb_token, users_request)
    print('59')
    imdb_result = imdb_data.results[0] if imdb_data else None
    db.add_to_history(message.from_user.id, users_request)
    if imdb_result:
        reply = f"Title: {imdb_result.title}\nDescription: {imdb_result.description}"
        await bot.send_photo(message.from_user.id,
                             imdb_result.image,
                             caption=reply)
        return
    else:
        await message.reply("Sorry, the movie couldn't be found")
        return



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
