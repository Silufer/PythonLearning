# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/29/2023 20:35
# @Author  : Ctsuhlu 
# @File    : fetch_async.py
# @Software: VS Code

import requests
from bs4 import BeautifulSoup
import time
import _thread
import os
from datetime import datetime
import json

url = 'https://www.youwu.cc/xiaoyu'
base_url = 'https://www.youwu.cc'
final_links = set()
img_links = set()
status = ''
date_format = "%Y-%m-%d %H:%M:%S"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577'
}


# 加载动画
def loading(lock):
    # 定义一个字符串列表，表示不同的加载符号
    loading_symbols = ['|', '/', '-', '\\']

    # 循环输出加载符号
    while lock[0]:
        for symbol in loading_symbols:
            # 使用 \r 把光标移动到行首，再输出加载符号
            print(f'\r{status} {symbol}', end='', flush=True)
            # 暂停 1 秒钟
            time.sleep(0.3)

# 检查更新
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

# 保存更新时间
def save_date():
    res = requests.get(url=url, headers=header)
    res.encoding = 'UTF-8'
    soup = BeautifulSoup(res.text, 'lxml')
    page = soup.select_one('html > body > div:nth-of-type(3) > div:nth-of-type(2) > ul > li:nth-of-type(1) > a')
    link = page.get('href')
    aurl = base_url + link
    res2 = requests.get(url=aurl, headers=header)
    res2.encoding = 'UTF-8'
    soup2 = BeautifulSoup(res2.text, 'lxml')
    page2 = soup2.select_one('html > body > div:nth-of-type(2) > div:nth-of-type(2) > span:nth-of-type(1)')
    raw = page2.text
    raw2 = raw.split('：')
    date = raw2[1]
    with open('data.json', 'w') as f:
        json.dump(date, f)

# 获取所有图片链接
def get_img_url():
    # 获取网页源码
    res = requests.get(url=url, headers=header)
    soup = BeautifulSoup(res.text, 'lxml')

    # 获取网页主链接
    divs = soup.find_all('div', attrs={'class': 'photo'})
    for div in divs:  # 一次解析
        link = div.find_all('a')
        for links in link:
            href = links.get('href')
            full_url = base_url + str(href)
            res2 = requests.get(url=full_url, headers=header)  # 二次解析
            soup2 = BeautifulSoup(res2.text, 'lxml')
            div2 = soup2.find_all('div', attrs={'class': 'page'})
            for div3 in div2:
                next_link = div3.find_all('a')
                for next_links in next_link:
                    if 'href' not in next_links.attrs:  # 去除无用的a标签
                        continue
                    else:
                        next_url = next_links.get('href')
                        cmb_link = base_url + str(next_url)
                        if cmb_link not in final_links:
                            final_links.add(cmb_link)

    # 获取图片链接
    for img in final_links:
        res3 = requests.get(url=img, headers=header)
        soup3 = BeautifulSoup(res3.text, 'lxml')
        img_url = soup3.find_all('a', attrs={'href': '#'})
        for img_urls in img_url:
            img_url2 = img_urls.find_all('img')
            for img_url3 in img_url2:
                src = img_url3.get('src')
                img_links.add(src)


# 下载图片
def download_img():
    for img_save in img_links:
        filename = str(img_save.split('/')[-1])
        img_res = requests.get(url=img_save, headers=header)
        with open('./pics/' + filename, 'wb') as f:
            f.write(img_res.content)


# 创建文件夹
def new_folder():
    folder_path = './pics'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def main():
    global status
    if check_update():
        b = input('有新的发布，是否下载（y/n）')
        if b == 'y':
            pass
        elif b == 'n':
            exit()
    else:
        a = input('没有新的发布, 输入q退出。')
        if a == 'q':
            exit()
    new_folder()
    status = '正在获取图片链接'
    start = time.time()
    lock = [True]
    _thread.start_new_thread(loading, (lock,))
    get_img_url()
    lock[0] = False
    end = time.time()
    hours = int((end - start) // 3600)
    minutes = int((end - start - hours * 3600) // 60)
    print('\r\n获取图片链接完成，耗时：', hours, 'h', minutes, 'min')
    status = '正在下载图片'
    start2 = time.time()
    lock = [True]
    _thread.start_new_thread(loading, (lock,))
    download_img()
    save_date()
    lock[0] = False
    end2 = time.time()
    hours2 = int((end2 - start2) // 3600)
    minutes2 = int((end2 - start2 - hours2 * 3600) // 60)
    print('\r\n下载图片完成，耗时：', hours2, 'h', minutes2, 'min')
    c = input('输入q退出。')
    if c == 'q':
        exit()

if __name__ == '__main__':
    main()
