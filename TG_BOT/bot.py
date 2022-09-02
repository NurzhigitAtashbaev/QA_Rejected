from telebot import TeleBot, types

from data import TOKEN


bot = TeleBot(TOKEN)


@bot.message_handlers(commands=['start'])
def start(message):
    buttons = types.InlineKeyboardMarkup()
    buttons.add(
        types.InlineKeyboardButton(
            'Посмотреть все курсы',
            callback_data='show_course_list',
        )
    )
    bot.send_message(message.chat.id, ' Привет!', reply_markup=buttons)


@bot.callback_query_handler(lambda c: c.data == 'show_course_list')
