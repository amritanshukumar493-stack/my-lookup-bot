import telebot
import requests
import urllib3
from telebot import types

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- SETTINGS ---
API_TOKEN = '8749792805:AAHoBfFoB2VlJiL1fP5hPfzO4NfQKa9ECao' # BotFather wala token
MY_USERNAME = "@LOSTED_EVERx"
MY_NAME = "⬎̸ 𝐋𝚶𝛅𝚻𝚬𝐃 𝚬𝐕𝚬𝐑𝚼𝚻𝚮𝚰𝚴𝐆 ❜ ⚚🏴‍☠️"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("💳 BUY PREMIUM API", url="https://t.me/LOSTED_EVERx")
    markup.add(btn1)
    bot.send_message(message.chat.id, f"<b>{MY_NAME}</b>\n\nStatus: <code>Online</code>\nUsage: Send Number.", parse_mode='HTML', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def get_info(message):
    number = message.text.strip()
    if not number.isdigit(): return
    
    sent_msg = bot.send_message(message.chat.id, "📡 <b>EXTRACTING...</b>", parse_mode='HTML')
    
    try:
        url = f"https://yash-code-with-ai.alphamovies.workers.dev/?num={number}&key=7189814021"
        response = requests.get(url, verify=False, timeout=20)
        data = response.json().get("0", response.json()) # Data extract

        result = (
            f"<b>┏━━━━━━🏴‍☠️ {MY_NAME} 🏴‍☠️━━━━━━┓</b>\n\n"
            f"  👤 <b>Name:</b> <pre>{data.get('name', 'N/A')}</pre>\n"
            f"  👨 <b>Father:</b> <pre>{data.get('fname', 'N/A')}</pre>\n"
            f"  🏠 <b>Address:</b> <pre>{data.get('address', 'N/A')}</pre>\n\n"
            f"<b>┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛</b>\n"
            f"<b>BY: {MY_USERNAME}</b>"
        )
        bot.edit_message_text(result, message.chat.id, sent_msg.message_id, parse_mode='HTML')
    except:
        bot.edit_message_text("❌ Server Error", message.chat.id, sent_msg.message_id)

# Bot ko Flask server ke sath wrap karna taki Render hamesha on rakhe
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "Bot is Alive!"

def run(): app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.polling(none_stop=True)
