import telebot
bot = telebot.TeleBot('5298905240:AAHkIzwAQb7X1wpZJD2v9neG8OxVFHzf64Y');
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, напиши что-нибудь')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, ' ' + message.text)
bot.polling(none_stop=True, interval=0)