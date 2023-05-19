# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 5/13/2023 2:10 PM
# @Author  : Ctsuhlu 
# @File    : dev_fetch.py.py
# @Software: Pycharm

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime
import json
import os
import time

url = 'https://www.youwu.cc/xiaoyu'
base_url = 'https://www.youwu.cc'


def ua():
    raw_user_agent = UserAgent()
    user_agent = raw_user_agent.random
    return user_agent


header = {
    'User-Agent': ua()
}


def check_update():
    if os.path.exists('data.json'):
        res = requests.get(url=url, headers=header)
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
        with open('data.json', 'r') as f:
            checkdate = json.load(f)
        old = datetime.strptime(checkdate["CheckDate"], '%Y-%m-%d %H:%M:%S')
        if old < new:
            return True
        else:
            return False
    else:
        return True

if __name__ == '__main__':
    if check_update():
        print('有新的发布')
    else:
        print('没有新的发布')
        time.sleep(3)
        exit()
