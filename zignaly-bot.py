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

# to authenticate to Zignaly and refresh the token
def getToken(force=False):
    global zignaly_token
    if zignaly_token == None or force:
        res = requests.post("https://zignaly.com/api/fe/api.php?action=login", json={
                            "email": config["username"], "password": config["password"], "projectId": "z01"}, headers=headers)
        body = json.loads(res.text)
        zignaly_token = body["token"]
    return zignaly_token

# Fetch all the open orders
def fetch_open_order():
    res = request_handler(
        "https://zignaly.com/api/fe/api.php?action=getOpenPositions&token=","GET")
    return json.loads(res)

# Fetch all the closed orders
def fetch_closed_order():
    res = request_handler(
        "https://zignaly.com/api/fe/api.php?action=getClosedPositions&token=","GET")
    return json.loads(res)

def fetch_status():
    res = request_handler(
        "https://zignaly.com/api/fe/api.php?action=getDashboardStats&token=","GET")
    return json.loads(res)

# Fetch balance of Zignaly profile
def fetch_balance():
    res = request_handler(
        "https://zignaly.com/api/fe/api.php?action=getBalance&token=","GET")
    return json.loads(res)
