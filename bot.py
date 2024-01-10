from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from os import getenv
load_dotenv()
bot = Bot(getenv('BOT'))
dp = Dispatcher()