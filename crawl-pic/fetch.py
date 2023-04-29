# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/03/2023 23:11
# @Author  : Ctsuhlu 
# @File    : fetch.py


import requests
from bs4 import BeautifulSoup
import time
import _thread
import os
from fake_useragent import UserAgent

url = 'https://www.youwu.cc/xiaoyu'
base_url = 'https://www.youwu.cc'
final_links = set()
img_links = set()
status = ''


# 随机生成User-Agent
def ua():
    raw_user_agent = UserAgent()
    user_agent = raw_user_agent.random
    return user_agent


hearder = {
    'User-Agent': ua()
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


# 获取所有图片链接
def get_img_url():
    # 获取网页源码
    res = requests.get(url=url, headers=hearder)
    soup = BeautifulSoup(res.text, 'lxml')

    # 获取网页标题
    # s = soup.find_all('p', {'class': 'title'})

    # 获取网页主链接
    divs = soup.find_all('div', attrs={'class': 'photo'})
    for div in divs:  # 一次解析
        link = div.find_all('a')
        for links in link:
            href = links.get('href')
            full_url = base_url + str(href)
            res2 = requests.get(url=full_url, headers=hearder)  # 二次解析
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
        res3 = requests.get(url=img, headers=hearder)
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
        img_res = requests.get(url=img_save, headers=hearder)
        with open('./pics/' + filename, 'wb') as f:
            f.write(img_res.content)


# 创建文件夹
def new_folder():
    folder_path = './pics'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def main():
    global status
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
    print('获取图片链接完成，耗时：', hours, 'h', minutes, 'min')
    status = '正在下载图片'
    start2 = time.time()
    lock = [True]
    _thread.start_new_thread(loading, (lock,))
    download_img()
    lock[0] = False
    end2 = time.time()
    hours2 = int((end2 - start2) // 3600)
    minutes2 = int((end2 - start2 - hours2 * 3600) // 60)
    print('下载图片完成，耗时：', hours2, 'h', minutes2, 'min')


if __name__ == '__main__':
    main()
