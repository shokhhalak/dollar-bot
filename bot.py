import telebot
import requests
import time
from datetime import datetime

TOKEN = '8496852583:AAFoFivJSDFKJoZJSq-oR1ztJL5RYS-vW14' 
CHANNEL_ID = '@heratdollar24'

bot = telebot.TeleBot(TOKEN)

def get_dollar_price():
    try:
        url = "https://api.tgju.org/v1/market/price/latest"
        response = requests.get(url, timeout=10)
        data = response.json()
        price = data['data']['price_dollar_rl']['p']
        price_afg = float(price) / 100
        return round(price_afg, 2)
    except:
        return 70.25

def send_price():
    price = get_dollar_price()
    time_now = datetime.now().strftime("%H:%M - %Y/%m/%d")
    
    message = f"""
💵 د ډالر نرخ - هرات

نن: {time_now}
بیه: {price} افغانۍ

#دالر #هرات #افغانستان
@heratdollar24
"""
    
    try:
        bot.send_message(CHANNEL_ID, message)
        print(f"✅ بیه ولیږل شوه: {price}")
    except Exception as e:
        print(f"❌ خطا: {e}")

if __name__ == "__main__":
    print("روبات چالان شو... د هرات ایلون مسک 👑")
    while True:
        send_price()
        time.sleep(1800)
