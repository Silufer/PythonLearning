# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/02/2023 22:13
# @Author  : Ctsuhlu
# @File    : get.py

import requests
from bs4 import BeautifulSoup

url = 'https://www.youwu.cc/xiaoyu'
base_url = 'https://www.youwu.cc'
hearder = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
final_links = set()
# 获取网页源码
res = requests.get(url=url, headers=hearder)
soup = BeautifulSoup(res.text, 'lxml')

# 获取网页标题
s = soup.find_all('p', {'class': 'title'})

# 获取网页主链接
divs = soup.find_all('div', attrs={'class': 'photo'})
for div in divs:
    link = div.find_all('a')
    for links in link:
        href = links.get('href')
        full_url = base_url + href
        res2 = requests.get(url=full_url, headers=hearder)
        soup2 = BeautifulSoup(res2.text, 'lxml')
        div2 = soup2.find_all('div', attrs={'class': 'page'})
        for div3 in div2:
            next_link = div3.find_all('a')
            for next_links in next_link:
                next_url = next_links.get('href')
                if base_url + next_url not in final_links:
                    final_links.add(base_url + next_link)
                    print(base_url + next_url)
