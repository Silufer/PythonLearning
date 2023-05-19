# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 5/18/2023 8:07 PM
# @Author  : Ctsuhlu 
# @File    : load date.py
# @Software: PyCharm

import json
from datetime import datetime

with open('data.json', 'r') as f:
    checkdate = json.load(f)

print(checkdate['CheckDate'])
print(type(checkdate['CheckDate']))

intdatetime = datetime.strptime(checkdate["CheckDate"], '%Y-%m-%d %H:%M:%S')
print(intdatetime)
print(type(intdatetime))
