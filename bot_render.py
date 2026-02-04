import os
import requests
import time
import random
from datetime import datetime

# Получаем токен из переменных окружения Render
TOKEN = os.environ.get("BOT_TOKEN", "8296574470:AAFUTpEzHUeAmIrSyluSi-D7YuwvaLgDaL8")
CHANNEL = os.environ.get("CHANNEL_ID", "-1003065388083")

print("=" * 50)
print("🤖 TELEGRAM BOT ON RENDER.COM")
print("=" * 50)
print(f"Channel: {CHANNEL}")
print("Posts: 09:00 and 19:00 MSK")
print("=" * 50)

# Факты
SEA_FACTS = [
    "🐙 Осьминоги имеют три сердца!",
    "🐋 Синий кит - самое большое животное!",
    "🦈 Акулы существуют 400 млн лет!"
]

SPACE_FACTS = [
    "🚀 На МКС 16 восходов в сутки!",
    "🪐 Сатурн мог бы плавать в воде!",
    "⭐ Звезда Бетельгейзе в 1000 раз больше Солнца!"
]

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        r = requests.post(url, data={"chat_id": CHANNEL, "text": text}, timeout=10)
        print(f"✅ Sent: {text[:30]}...")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# Тест
send_message("🚀 Bot deployed on Render.com! Running 24/7")

print("\nBot is running...")

while True:
    now = datetime.utcnow()  # Render использует UTC!
    hour = now.hour
    minute = now.minute
    
    # 9:00 МСК = 6:00 UTC
    if hour == 6 and minute == 0:
        fact = random.choice(SEA_FACTS)
        send_message(f"🌅 Доброе утро!\n\n{fact}\n\n#море")
        time.sleep(61)
    
    # 19:00 МСК = 16:00 UTC
    elif hour == 16 and minute == 0:
        fact = random.choice(SPACE_FACTS)
        send_message(f"🌙 Добрый вечер!\n\n{fact}\n\n#космос")
        time.sleep(61)
    
    time.sleep(30)
