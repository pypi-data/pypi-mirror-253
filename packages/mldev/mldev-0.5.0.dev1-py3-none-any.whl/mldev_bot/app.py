# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

import sh
import telebot
import yaml
import os, sys

from mldev_bot.proxy import current_proxy

telebot.apihelper.proxy = {'https': 'socks{}://{}:{}'.format(current_proxy.get('version'),
                                                             current_proxy.get('ip'),
                                                             current_proxy.get('port'))}

bot_token = sys.argv[1]
need_warnings = True if sys.argv[2].lower() == "true" else False

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     'Привет, я бот для отслеживания работы твоего проекта через систему ml_dev. Буду сообщать тебе\
                     об ошибках, произошедших во время выполнения проекта. Чтобы остановить меня, кликни /stop.')

    log_reading(chat_id)


def log_reading(chat_id):
    path_to_stderr = os.path.dirname(os.path.abspath(__file__))
    stderr_filename = os.path.join(path_to_stderr, 'logs/stderr.txt')

    _tail = sh.tail("-f", stderr_filename, _iter=True)
    while True:
        new_line = _tail.next()
        if not new_line.isspace():
            if need_warnings and "warning" in new_line.lower():
                bot.send_message(chat_id, "Предупреждение: {}".format(new_line))
            elif "error" in new_line.lower() or "exception" in new_line.lower():
                bot.send_message(chat_id, "Ошибка при выполнении: {}".format(new_line))


@bot.message_handler(commands=['stop'])
def stop_log_reading(message):
    bot.send_message(message.chat.id, "Чтение логов и бот остановлены")
    os.system('kill %d' % os.getpid())


if __name__ == '__main__':
    bot.polling(none_stop=True)
