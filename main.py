from bot import bot, dp
from handlers.crosswords_handler import crosswords_rt
import asyncio


async def main():
    dp.include_router(crosswords_rt)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
