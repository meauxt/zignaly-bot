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