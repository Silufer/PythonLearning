# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/01/2023 23:24
# @Author  : Ctsuhlu 
# @File    : hitokoto.py

import requests
import os
import time

url = 'https://v1.hitokoto.cn'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5410.0 Safari/537.36'
}
def get():
    global res
    raw_res = requests.get(url=url, headers=header)
    res = raw_res.json()

def clear():
    os.system('cls')

def loading():
    print("\r加载中", end="")
    for i in range(3):
        print(".", end='', flush=True)
        time.sleep(0.3)
    
def main():
    while True:
        get()
        loading()
        clear()
        print(res['hitokoto'], '——————', res['from'])
        a = input('\n按回车键继续, 输入q退出。')
        if a == 'q':
            exit()
        clear()

if __name__ == '__main__':
    main()
