import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import config
from tiktok import get_tiktok_stats
from db import init_db, save_stats

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer(f"📊 Отслеживаю TikTok @{config.TIKTOK_USERNAME}")
    await send_stats(message.chat.id)

async def send_stats(chat_id):
    now = datetime.now().strftime("%Y-%m-%d")
    stats = get_tiktok_stats(config.TIKTOK_USERNAME)
    save_stats(now, stats["followers"], stats["likes"], stats["videos"])

    msg = (
        f"📊 TikTok Stats @{config.TIKTOK_USERNAME}\n\n"
        f"👥 Подписчики: {stats['followers']}\n"
        f"❤️ Лайки: {stats['likes']}\n"
        f"🎞️ Видео: {stats['videos']}"
    )

    await bot.send_message(chat_id, msg)

async def main():
    init_db()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_stats, "cron", hour=12, args=[config.OWNER_CHAT_ID])
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
