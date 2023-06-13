# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 06/13/2023 21:22
# @Author  : Ctsuhlu 
# @File    : test_timer.py
# @Software: VS Code

import time
import _thread

def loading(lock):
    loading_symbols = ['|', '/', '-', '\\']

    while lock[0]:
        for symbol in loading_symbols:
            print(f'\r{status} {symbol}', end='', flush=True)
            time.sleep(0.3)

status = '加载中'
start = time.time()
lock = [True]
_thread.start_new_thread(loading, (lock,))
time.sleep(3720)  # 设置模拟工作时间
lock[0] = False
end = time.time()
hours = int((end - start) // 3600)
minutes = int((end - start - hours * 3600) // 60)
print('\r\n已完成，耗时：', hours, 'h', minutes, 'min')
