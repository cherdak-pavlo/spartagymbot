import telebot
from telebot import types

token = '1782223806:AAERz5EaedypUy5xfQPxv2W-Dd7zG4h2rtQ'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Пропали кнопки керування ботом?', callback_data='miss_buttons')
    markup.add(item1)
    bot.send_message(message.chat.id, "Якщо немає вашого питання в списку, зв'яжіться з @killcrop123",
                     reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🕒 Графік роботи')
    button2 = types.KeyboardButton('💰 Вартість тренування/абонементу')
    button3 = types.KeyboardButton('🏋️ Хочу почати тренуватися')
    button4 = types.KeyboardButton('📞 Контакти')
    markup.add(button2)
    markup.add(button3)
    markup.add(button1, button4)
    bot.send_message(message.chat.id, "<b>Вітаємо, {0.first_name}!</b>\n"
                                      "Нижче знаходяться кнопки для керування чат-ботом.\n"
                                      "Якщо виникли проблеми у користуванні ботом - напишіть в чат команду /help".format(
        message.from_user), reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == '🕒 Графік роботи':
        bot.send_message(message.chat.id, '<i><b>Увага❗</b>З 25 березня діє "червоний" рівень епіднебезпеки.\n'
                                          'Працюємо лише за попереднім індивідуальним записом.\n'
                                          'Щодо запису - звертатися за контактним номером телефону.</i>\n\n'
                                          'Понеділок: <b>16:00 - 22:00</b>\n'
                                          'Вівторок: <b>16:00 - 19:00</b>\n'
                                          'Середа: <b>16:00 - 22:00</b>\n'
                                          'Четвер: <b>16:00 - 19:00</b>\n'
                                          "П'ятниця: <b>16:00 - 22:00</b>\n"
                                          "Субота: <b>Вихідний</b>\n"
                                          "Неділя: <b>Вихідний</b>", parse_mode='html')

    elif message.text == '🏋️ Хочу почати тренуватися':
        markup = types.InlineKeyboardMarkup(row_width=3)
        item1 = types.InlineKeyboardButton('Ніколи не тренувався в тренажерному залі', callback_data='first')
        item2 = types.InlineKeyboardButton('Тренувався, але потрібна допомога тренера', callback_data='new')
        item3 = types.InlineKeyboardButton('Маю достатньо досвіду', callback_data='normal')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, 'Виберіть ваш рівень підготовки:', reply_markup=markup)

    elif message.text == '💰 Вартість тренування/абонементу':
        bot.send_message(message.chat.id, 'Разове тренування - <b><i>20 грн.</i></b>\n'
                                          'Абонемент на місяць - <b><i>200 грн.</i></b>\n\n'
                                          '<i>Для початківців діє спеціальна пропозиція 🔥\n'
                                          'При купівлі абонементу на місяць наш тренер <u>безкоштовно</u> допоможе Вам скласти індивідальну програму тренувань.</i>',
                         parse_mode='html')

    elif message.text == '📞 Контакти':
        bot.send_message(message.chat.id, '+380673731324 Юрій Васильович', parse_mode='html')

        bot.send_photo(message.chat.id, open(r'C:\Users\Killcrop123\PycharmProjects\SpartaGymBot\Photos\location.jpg', 'rb').read(),
                       caption='<i>м.Львів, вул. Кирила Трильовського 16</i>', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Поки я не знаю що на це відповісти :(\n'
                                          'Якщо у Вас виникли проблеми у користуванні ботом - напишіть в чат команду /help')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'first':
                bot.send_message(call.message.chat.id, 'Для того що б почати тренуватися Вам необхідно:\n'
                                                       '1. Поїсти за 2-3год. до початку тренування\n'
                                                       '2. Взяти з собою воду, перезувне, та спортивну форму(шорти/штани + футболка/олімпійка)\n'
                                                       '3. А також не забути про хороший настрій та мотивацію 😉\n\n'
                                                       'До зустрічі на тренуванні 💪', parse_mode='html')

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='<i>Перше тренування для новачків є <u>безкоштовне.</u></i>\n'
                                           '<i>На перше тренування бажано приходити у будні в період <b>17:00 - 19:00</b></i>\n',
                                      reply_markup=None, parse_mode='html')

            elif call.data == 'new':
                bot.send_message(call.message.chat.id, "Також декілька корисних порад:\n"
                                                       "1. Будь-яке тренування повинне починатися з розминки\n"
                                                       "2. Оптимальна кількість тренувань на тиждень - три рази\n"
                                                       "3. Кожному спортсмену потрібна індивідуальна програма тренувань\n"
                                                       "<i>(З цим Вам допоможе наш тренер)</i>\n"
                                                       "4. Хороший сон і правильне харчування - невід'ємні атрибути майбутнього успіху\n\n"
                                                       "До зустрічі на тренуванні 💪", parse_mode="html")

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<i>Що б отримати допомогу тренера - приходьте у будні в період <b>17:00 - 19:00</b></i>",
                                      reply_markup=None, parse_mode='html')

            elif call.data == 'normal':
                bot.send_message(call.message.chat.id, 'Зал працює згідно з графіком\n'
                                                       'Також не забувайте прибирати за собою інвентар :)\n\n'
                                                       'До зустрічі на тренуванні 💪')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Просимо звернути увагу❗️</b>\n"
                                           "<i>При купівлі абонементу на місяць ви заощаджуєте кошти!</i>",
                                      reply_markup=None, parse_mode='html')

            elif call.data == 'miss_buttons':
                bot.send_photo(call.message.chat.id,
                               open(r"C:\Users\Killcrop123\PycharmProjects\GymSpartaBot\Photos\miss_button.jpg",
                                    'rb').read(), caption='<i>Пропали кнопки керування ботом?</i>\n'
                                                          '<b>Відповідь:</b> Натисніть на цей значок, як на фото',
                               parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Надіємося ми змогли Вам допомогти 🙂", reply_markup=None)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
