🔧 Установка и запуск на Render.com

1. Зайди на https://render.com
2. Создай новый "Web Service" → подключи GitHub или загрузи ZIP
3. Установи Build Command: `pip install -r requirements.txt`
4. Установи Start Command: `python bot.py`
5. Укажи переменные окружения или редактируй config.py:
   - BOT_TOKEN = твой токен от BotFather
   - OWNER_CHAT_ID = твой Telegram chat_id
6. Всё! Бот будет запускаться сам.

📌 Для получения chat_id:
   - Напиши /start своему боту
   - Временно добавь в start_cmd:
     `print(message.chat.id)`

📌 Статистика обновляется каждый день в 12:00 (по времени сервера).