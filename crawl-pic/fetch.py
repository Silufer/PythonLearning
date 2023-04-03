# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/02/2023 22:13
# @Author  : Ctsuhlu
# @File    : get.py

import requests
from bs4 import BeautifulSoup
import time
import _thread
import os

url = 'https://www.youwu.cc/xiaoyu'
base_url = 'https://www.youwu.cc'
hearder = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
final_links = set()
img_links = set()

def loading(lock):
    chars = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 0
    while lock[0]:
        i = (i+1) % len(chars)
        print('\033[A%s %s' %
              (chars[i], lock[1] or '' if len(lock) >= 2 else ''))
        time.sleep(0.25)
    print('')

print('正在获取图片链接...')
lock = [True]
_thread.start_new_thread(loading, (lock,))

new_folder = './pics'
os.mkdir(new_folder)

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
        full_url = base_url + str(href)
        res2 = requests.get(url=full_url, headers=hearder)
        soup2 = BeautifulSoup(res2.text, 'lxml')
        div2 = soup2.find_all('div', attrs={'class': 'page'})
        for div3 in div2:
            next_link = div3.find_all('a')
            for next_links in next_link:
                if 'href' not in next_links.attrs:
                    continue
                else:
                    next_url = next_links.get('href')
                    cmb_link = base_url + str(next_url)
                    if cmb_link not in final_links:
                        final_links.add(cmb_link)

# 获取图片
for img in final_links:
    res3 = requests.get(url=img, headers=hearder)
    soup3 = BeautifulSoup(res3.text, 'lxml')
    img_url = soup3.find_all('a', attrs={'href': '#'})
    for img_urls in img_url:
        img_url2 = img_urls.find_all('img')
        for img_url3 in img_url2:
            src = img_url3.get('src')
            img_links.add(src)

lock[0] = False

print('正在下载图片...')
lock = True
_thread.start_new_thread(loading, (lock,))

for img_save in img_links:
    filename = str(img_save.split('/')[-1])
    img_res = requests.get(url=img_save, headers=hearder)
    with open('./pics/' + filename, 'wb') as f:
        f.write(img_res.content)

lock = False
