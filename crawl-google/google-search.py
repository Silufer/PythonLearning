# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 3/19/2023 8:17 AM
# @Author  : Ctsuhlu
# @File    : google-search.py

import requests

if __name__ == '__main__':
    url = 'https://www.google.com/search'
    param = {
        'q': input('Search:')
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5410.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=header, params=param)
    page_txt = response.text
    with open('./data.html', 'w', encoding='utf-8') as fp:
        fp.write(page_txt)
    print('Done!')
