import os

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [str(os.getenv("admin_id"))]
imdb_token = str(os.getenv("imdb_token"))
