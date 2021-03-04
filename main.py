from core.settings import bot


@bot.message_handler(commands=['info'])
def send_chat_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f'Your chat id is: {chat_id}')


bot.polling()
