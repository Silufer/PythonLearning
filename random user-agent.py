# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/02/2023 02:33
# @Author  : Ctsuhlu 
# @File    : random user-agent.py

from fake_useragent import UserAgent
raw_user_agent = UserAgent(browsers=['edge', 'chrome'])
user_agent = raw_user_agent.random
print(user_agent)
