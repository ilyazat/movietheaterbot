from aiogram import executor

from set_bot_commands import set_default_commands
from notify_admins import on_startup_notify
from loader import dp

# TODO:
#  - Code-architecture lol
#  - Deploy on AWS
#  - Add inline0-buttons
#  - Cover bot with unit-tests
#  - Add support of kinopoisk
#  - Add distinguishing between languages to select API (only for russian: kinopoisk.ru)
#  - Add fetching online video services by request
#  - Add fetching of random movie-title and information about it ("I don't know what to watch!")


async def on_startup(disp):
    await on_startup_notify(disp)
    await set_default_commands(disp)


if __name__ == '__main__':
    from users import dp
    executor.start_polling(dp, on_startup=on_startup)
