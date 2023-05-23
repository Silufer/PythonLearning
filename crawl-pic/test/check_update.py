# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 5/23/2023 12:16 AM
# @Author  : Ctsuhlu 
# @File    : check_update.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import json

url = 'https://www.youwu.cc/xiaoyu'
base_url = 'https://www.youwu.cc'
date_format = "%Y-%m-%d %H:%M:%S"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577'
}

def check_update():
    if os.path.exists('data.json'):  # 判断文件是否存在
        res = requests.get(url=url, headers=header)  # 获取最新更新时间
        res.encoding = 'UTF-8'
        soup = BeautifulSoup(res.text, 'lxml')
        page = soup.select_one('html > body > div:nth-of-type(3) > div:nth-of-type(2) > ul > li:nth-of-type(1) > a')
        link = page.get('href')
        aurl = base_url+link
        res2 = requests.get(url=aurl, headers=header)
        res2.encoding = 'UTF-8'
        soup2 = BeautifulSoup(res2.text, 'lxml')
        page2 = soup2.select_one('html > body > div:nth-of-type(2) > div:nth-of-type(2) > span:nth-of-type(1)')
        raw = page2.text
        raw2 = raw.split('：')
        date = raw2[1]
        new = datetime.strptime(date, date_format)
        with open('data.json', 'r') as f:  # 读取时间记录文件
            checkdate = json.load(f)
        old = datetime.strptime(checkdate, '%Y-%m-%d %H:%M:%S')
        if old < new:  # 比较时间
            return True
        else:
            return False
    else:
        return True

print(check_update())
