#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8080798222:AAFUfsajFp_vOeiF2eE-ituTbZ4HfIRKp20")
    API_ID = int(os.environ.get("API_ID", "23454876"))
    API_HASH = os.environ.get("API_HASH", "b42626ee535fcaf915232af564a95bea")
    AUTH_USERS = "662494886"

