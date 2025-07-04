import os
import telegram

def send_telegram_message(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    message = "Your message here"
    bot.send_message(chat_id=chat_id, text=message)
    return "Message sent"
