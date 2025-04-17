#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6216840269:AAFNzApyRlXuZ94T3UZgd-XqNun2mA40kJU")
    API_ID = int(os.environ.get("API_ID", "23454876"))
    API_HASH = os.environ.get("API_HASH", "b42626ee535fcaf915232af564a95bea")
    AUTH_USERS = "1411895712"

