import logging
import os
import random

import dialogs
import telebot
from flask import request, Flask
from telebot import types

import constants
import picurl

bot = telebot.TeleBot(constants.TOKEN)


# обработчик команды /start
# добавляем встроенную клавиатуру
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_registration = types.KeyboardButton('💍 Регистрация 💐')
    button_banquet = types.KeyboardButton('🥂 Банкет 🍽')
    button_dresscode = types.KeyboardButton('👗 Дресс-код 👔')
    button_media = types.KeyboardButton('📸 Фото и видео 🎥')
    button_team = types.KeyboardButton('Наша команда')
    button_young = types.KeyboardButton('О нас')
    markup.row(button_registration, button_banquet)
    markup.row(button_dresscode, button_media)
    markup.row(button_team, button_young)
    if message.chat.id != constants.GROUP_ID:
        bot.send_message(message.from_user.id, "Выбери пункт меню 👇", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "Выбери пункт меню 👇", reply_markup=markup)
        bot.reply_to(message, 'Смотри личное сообщение!')


# обработчик команды /about
@bot.message_handler(commands=['about'])
def message_about(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Статья о роботе Марвине на Wikipedia.org',
                                            url=' ')
    keyboard.add(url_button)
    if message.chat.id != constants.GROUP_ID:
        bot.send_message(message.from_user.id, dialogs.s_about, parse_mode='html', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, dialogs.s_about, parse_mode='html', reply_markup=keyboard)
        bot.reply_to(message, 'Ответил в личном сообщении!')


# обработчик команды /help
@bot.message_handler(commands=['help'])
def message_about(message):
    if message.chat.id != constants.GROUP_ID:
        bot.send_message(message.from_user.id, dialogs.s_help, parse_mode='html')
    else:
        bot.send_message(message.from_user.id, dialogs.s_help, parse_mode='html')
        bot.reply_to(message, 'Проверь личное сообщении!')


@bot.message_handler(content_types=['text'])
def send_message_main(message):
    # приветствие бота
    if message.text.lower() == 'бот' or message.text.lower() == 'марвин' or message.text.lower() == 'bot' or \
            message.text.lower() == 'marvin':
        bot.send_message(message.chat.id, '<i>Вызывали? 🤖</i>\n'
                                          '<b>Приветствую тебя дорогой друг!</b>'
                                          '\n\nНажми на эту ссылку @WeddingInfo_bot, а затем кнопку для запуска '
                                          'и я расскажу тебе в личном сообщении о событии, которое состоится 10 октября '
                                          'этого года!'
                                          '\n\nОстальные вопросы ты можешь уточнить в общем чате у кожаных мешков '
                                          'Евгении и Максима!', parse_mode='html')
    # # прощание с ботом
    # elif dialogs.func_dialogs(message.text):
    #     bot.reply_to(message, dialogs.func_dialogs(message.text))
    # мат-фильтр
    elif set(message.text.lower().split()) & dialogs.S_censored_words:
        bot.reply_to(message, random.choice(dialogs.L_response_from_bot) + ' 🤬')
    elif message.text == 'date_here':
        bot.reply_to(message, 'Красивая дата!')
    # меню регистрация
    elif message.text == '💍 Регистрация 💐' or message.text.lower() == 'регистрация':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Посмотреть на карте 2ГИС', url=' ')
        keyboard.add(url_button)
        bot.send_message(message.from_user.id, '<b>Место проведения:</b> Кремль\n'
                                               '<b>Сбор гостей для фотосессии:</b> 16:00\n'
                                               '<b>Начало церемонии:</b> 16:30\n\n'
                                               'На месте проведения церемонии будет расположена Welcome зона с '
                                               'прохладительными напитками',
                         parse_mode='html',
                         reply_markup=keyboard)
        bot.send_location(message.from_user.id, latitude=46.349619, longitude=48.030969)
    # меню Банкет
    elif message.text == "🥂 Банкет 🍽" or message.text.lower() == 'банкет':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Посмотреть на карте 2ГИС', url=' ')
        keyboard.add(url_button)
        bot.send_message(message.from_user.id, '<b>Место проведения:</b> банкетный зал " " '
                                               '(3 этаж), ул.\n'
                                               '<b>Сбор гостей:</b> 17:30\n'
                                               '<b>Начало мероприятия:</b> 18:00',
                         parse_mode='html', reply_markup=keyboard)
        bot.send_location(message.from_user.id, latitude=46.350083, longitude=48.041742)
    # меню Дресс-код
    elif message.text == '👗 Дресс-код 👔' or message.text.lower() == 'дресс-код':
        palette1 = picurl.palette1
        palette2 = picurl.palette2
        palette3 = picurl.pallete3
        dresscode1 = picurl.dresscode1
        bot.send_message(message.from_user.id, '<b>Уважаемые дамы</b>, мы будем рады, если ваши платья будут близки к '
                                               'нашей цветовой палитре ☺️!\n'
                                               '<b>Уважаемые джентельмены</b>, будем признательны, если вы выберете '
                                               'официально-деловой стиль одежды (бабочки друзьям жениха будут '
                                               'предоставлены)', parse_mode='html')
        media = [types.InputMediaPhoto(palette1, "Цветовая палитра мероприятия"),
                 types.InputMediaPhoto(palette2, "Цветовая палитра мероприятия"),
                 types.InputMediaPhoto(palette3, "Цветовая палитра мероприятия"),
                 types.InputMediaPhoto(dresscode1, "Пример дресс-кода")]
        bot.send_media_group(message.from_user.id, media)
    # меню Фото и видео
    elif message.text == '📸 Фото и видео 🎥' or message.text.lower() == 'фото и видео':
        bot.send_message(message.from_user.id, 'Ссылки на соответствующие материалы появятся по окончанию торжества')
    # меню Наша команда
    elif message.text.lower() == 'Наша команда' or message.text.lower() == 'наша команда':
        kashirin = picurl.kashirin
        kashirina = picurl.kashirina
        baitelman = picurl.baitelman
        blinov = picurl.blinov
        shafeeva = picurl.shafeeva
        bot.send_message(message.from_user.id, 'Наша команда по подготовке и созданию торжества:', parse_mode='html')
        media = [types.InputMediaPhoto(kashirin, "- ведущий"),
                 types.InputMediaPhoto(kashirina, "  - организатор"),
                 types.InputMediaPhoto(baitelman, "  - фотограф"),
                 types.InputMediaPhoto(blinov, " - видеограф"),
                 types.InputMediaPhoto(shafeeva, "  - дизайнер")]
        bot.send_media_group(message.from_user.id, media)
    # Информация о молодых
    elif message.text == 'О нас' or message.text.lower() == 'о нас':
        keyboard = types.InlineKeyboardMarkup()
        insta_evgenia = types.InlineKeyboardButton(text='Женя Instagram',
                                                   url=' ')
        insta_maksim = types.InlineKeyboardButton(text='Макс Instagram',
                                                  url=' ')
        vk_evgenia = types.InlineKeyboardButton(text='Женя vkontakte',
                                                url=' ')
        vk_maksim = types.InlineKeyboardButton(text='Макс vkontakte',
                                               url=' ')
        face_evgenia = types.InlineKeyboardButton(text='Женя facebook',
                                                  url=' ')
        face_maksim = types.InlineKeyboardButton(text='Макс facebook',
                                                 url=' ')
        keyboard.add(insta_evgenia, insta_maksim)
        keyboard.add(vk_evgenia, vk_maksim)
        keyboard.add(face_evgenia, face_maksim)
        bot.send_message(message.from_user.id, dialogs.s_about_youg, parse_mode='html',
                         reply_markup=keyboard)


if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)


    @server.route('/' + constants.TOKEN, methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url=' ' + constants.TOKEN)
        return "!", 200


    if __name__ == '__main__':
        server.debug = True
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)

# if __name__ == "__main__":
#     # bot.remove_webhook()
#     bot.polling(none_stop=True, interval=0)
