from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import config
from tiktok import get_tiktok_stats
from db import init_db, save_stats, get_last_stats

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer(f"📊 Отслеживаю статистику TikTok аккаунта @{config.TIKTOK_USERNAME}")
    await send_stats(message.chat.id)

async def send_stats(chat_id):
    now = datetime.now().strftime("%Y-%m-%d")
    stats = get_tiktok_stats(config.TIKTOK_USERNAME)
    save_stats(now, stats["followers"], stats["likes"], stats["videos"])

    msg = f"📊 TikTok Stats @{config.TIKTOK_USERNAME}\n\n"
    msg += f"👥 Подписчики: {stats['followers']}\n"
    msg += f"❤️ Лайки: {stats['likes']}\n"
    msg += f"🎞️ Видео: {stats['videos']}\n"

    await bot.send_message(chat_id, msg)

def schedule_jobs():
    scheduler.add_job(send_stats, "cron", hour=12, args=[config.OWNER_CHAT_ID])
    scheduler.start()

if __name__ == "__main__":
    init_db()
    schedule_jobs()
    executor.start_polling(dp)