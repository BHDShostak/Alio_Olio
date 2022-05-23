import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("BOOKING A TABLE")
    item4 = types.KeyboardButton("WRITE TO US")
    item5 = types.KeyboardButton("CONTACT DETAILS")

    markup.add(item1, item4, item5)

    bot.send_message(message.chat.id,
                     "Hello {0.first_name}!,\nWelcome in <b>{1.first_name}</b> Restaurant.\nWhat i can do for "
                     "you?\nOn the bottom you can choose option ↓".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup
                     )


reservations = []
tables = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@bot.message_handler(content_types=['text'])
def answer1(message):
    if message.text == 'BOOKING A TABLE':
        if len(reservations) == 0:
            for table in tables:
                reservations.append(table)
                print(bot.send_message(message.chat.id, 'Yours table number is ' + str(table) +
                                       ' {0.first_name}! \nThank you for reservation!'.format(message.from_user,
                                                                                              bot.get_me()),
                                       parse_mode='html'
                                       ))
                break

        elif len(reservations) >= 10:
            bot.send_message(message.chat.id, 'All tables reserved!')
        elif len(reservations) <= 10:
            for table in tables:
                if table in reservations:
                    pass
                else:
                    reservations.append(table)
                    print(bot.send_message(message.chat.id, 'Yours table number is' + str(table) +
                                           ' {0.first_name}! \nThank you for reservation!'.format(message.from_user,
                                                                                                  bot.get_me()),
                                           parse_mode='html'
                                           ))
                    break

    elif message.text == 'WRITE TO US':
        bot.send_message(message.chat.id, 'RESTAURANT@ALIO_OLIO.COM'.format(message.from_user,
                                                                            bot.get_me()), parse_mode='html'
                         )
    elif message.text == 'CONTACT DETAILS':
        bot.send_message(message.chat.id,
                         'TEL: +48570755078\nAdress: Markowskiego 10,31-332 CRACOW,POLAND'.format(
                             message.from_user,
                             bot.get_me()), parse_mode='html'
                         )
    else:
        bot.send_message(message.chat.id, 'YOUR TABLE WAS NOT RESERVETED OR DO NOT UNDERSTAND YOU')


bot.polling(none_stop=True)
