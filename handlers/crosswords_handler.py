from aiogram import Router, types
from bot import bot


crosswords_rt = Router()
crosswords = ['мат1', 'bezmozglyi', 'durachok', 'мат2']


@crosswords_rt.message()
async def crwrds_hndlr(message: types.Message):
    message_list = message.text.split()
    #Разбил, чтобы проверить каждое слово в тексте
    for i in message_list:
        i = i.lower()
        if i in crosswords:
            await bot.ban_chat_member(chat_id=message.chat.id,
                                      user_id=message.from_user.id)
