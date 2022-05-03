import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("BOOKING A TABLE")
    item2 = types.KeyboardButton("CANCELLATION OF THE RESERVATION")
    item4 = types.KeyboardButton("WRITE TO US")
    item5 = types.KeyboardButton("CONTACT DETAILS")




    markup.add(item1, item2,item4,item5)

    bot.send_message(message.chat.id,
                     "Hello {0.first_name}!,\nWelcome in <b>{1.first_name}</b> Restaurant.\nWhat i can do for you?\nOn the bottom you can choose option ↓".format(
                     message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup= markup
                     )

tables = []
lenth = len(tables)

@bot.message_handler(content_types=['text'])
def answer1(message):
    global name1
    if message.chat.type == 'private':
        if message.text == 'BOOKING A TABLE':
            randomNumber1 = int(random.randint(1, 15))


            if lenth == 0:
                tables.append(randomNumber1)
                bot.send_message(message.chat.id, 'Yours table number is ' + str(randomNumber1) +
                                 ' {0.first_name}! \nThank you for reservation!'.format( message.from_user, bot.get_me()),
                                 parse_mode='html'
                                 )
            elif lenth >= 10:
                bot.send_message(message.chat.id,'All tables reserved!')
            else:
                for index2 in tables:
                    if index2[tables] == randomNumber1:
                        continue
                    else:
                        tables.append(randomNumber1)
                        bot.send_message(message.chat.id, 'Yours table number is ' + str(randomNumber1) +
                                         ' {0.first_name}! \nThank you for reservation!'.format(message.from_user,
                                         bot.get_me()),parse_mode='html'
                                         )

        elif message.text == 'CANCELLATION OF THE RESERVATION':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("1", callback_data='1')
            item2 = types.InlineKeyboardButton("2", callback_data='2')
            item3 = types.InlineKeyboardButton("3", callback_data='3')
            item4 = types.InlineKeyboardButton("4", callback_data='4')
            item5 = types.InlineKeyboardButton("5", callback_data='5')
            item6 = types.InlineKeyboardButton("6", callback_data='6')
            item7 = types.InlineKeyboardButton("7", callback_data='7')
            item8 = types.InlineKeyboardButton("8", callback_data='8')
            item9 = types.InlineKeyboardButton("9", callback_data='9')
            item10 = types.InlineKeyboardButton("10", callback_data='10')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

            bot.send_message(message.chat.id, 'Can you give me your number of the table?', reply_markup=markup)

        elif message.text == 'WRITE TO US':
            bot.send_message(message.chat.id, 'RESTAURANT@ALIO_OLIO.COM'.format(message.from_user,
                            bot.get_me()), parse_mode='html'
                             )
        elif message.text == 'CONTACT DETAILS':
            bot.send_message(message.chat.id, 'TELEPHONE: +48570755078\nADRESS: MARKOWSKIEGO 10,31-332 CRACOW,POLAND'.format(message.from_user,
                            bot.get_me()), parse_mode='html'
                             )
        else:
            bot.send_message(message.chat.id, 'YOUR TABLE WAS NOT RESERVETED OR DO NOT UNDERSTAND YOU')

@bot.message_handler(commands=['start'])
def removeKeyBoard(message):
    bot.sendMessage(
      chat_id,
      reply_markup = ReplyKeyboardRemove()
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            bot.send_message(call.message.chat.id, 'Your reservation, was canceled,\nSee you soon!')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="CANCELLATION OF THE RESERVATION",
                              reply_markup=None)

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                              text="Massage was sended!")

    except Exception as e:
        print(repr(e))





bot.polling(none_stop=True)