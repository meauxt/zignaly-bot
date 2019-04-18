from __future__ import division

import atexit

import time as ptime
import requests
import json
import sys
import os
import threading
import math
from datetime import datetime, date, time

import timeago
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import telegram
import telepot
from datetime import datetime, timedelta
from binance.client import Client


# Telegram bot initilizer.. will send message when the bot able to connect


def init_telegram():
    global telegram_bot
    telegram_bot = telepot.Bot(config["telegram_token"])
    try:
        telegram_bot.sendMessage(chat_id=config["chat_id"], text="Bot started! (Notification is off by default)",
                                 parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=getReplyKeyboard())
    except Exception as e:
        print("Unable to load telegram plugin.. please check you provide valid bot token in config.json")
        print(e)
    MessageLoop(telegram_bot, messageHandler).run_as_thread()
# Telegram bot initilizer.. will send message when the bot able to connect
def init_config():
    global config
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
    except Exception as e:
        print(
            "Error reading config.json..check if the file is valid json or if it's existed")
      