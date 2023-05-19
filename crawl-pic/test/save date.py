# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 5/18/2023 8:02 PM
# @Author  : Ctsuhlu 
# @File    : dev.py
# @Software: PyCharm

import json
from datetime import datetime

checkdate = {
    "CheckDate": "2023-04-08 21:07:07",
}

with open('data.json', 'w') as f:
    json.dump(checkdate, f)
