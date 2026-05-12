from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def home(): return "Herat Dollar Bot is Alive"
Thread(target=lambda: app.run(host='0.0.0.0',port=10000)).start()

# ===== ستا د روبات اصل کوډ له دې ځایه شروع کیږي =====
import telebot
import requests
import time
from datetime import datetime
import os

TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

bot = telebot.TeleBot(TOKEN)8539566565:AAGoVxTZnjoi_kfXNS2qe66V2BnsF2lPuog

def get_dollar_price():
    try:
        url = "https://api.tgju.org/v1/market/indicator/summary-table-data/price_dollar_rl"
        response = requests.get(url, timeout=10)
        data = response.json()
        price = data['data']['price']
        price_afg = float(price) / 100
        return round(price_afg, 2)
    except:
        return None

def send_price():
    price = get_dollar_price()
    if price:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = f"💵 د ډالر اوسنۍ بیه:\n\n1 USD = {price} افغانۍ\n\n⏰ وخت: {now}\n@heratdollar24"
        bot.send_message(CHANNEL_ID, text)

while True:
    send_price()
    time.sleep(1800)  # هر 30 دقیقه
