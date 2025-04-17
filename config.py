#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7744338796:AAEmp0R9sUSIXfhHgJMwOnaYfNCPYgZUW24")
    API_ID = int(os.environ.get("API_ID", "22410340"))
    API_HASH = os.environ.get("API_HASH", "633122e0c3b0100c2ec829e8a52e6a51    ")
    AUTH_USERS = "662494886,1202982274"

