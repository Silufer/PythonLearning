# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/01/2023 23:34
# @Author  : Ctsuhlu 
# @File    : loading 2.py

import time

# 定义一个字符串列表，表示不同的加载符号
loading_symbols = ['|', '/', '-', '\\']

# 循环输出加载符号
while True:
    for symbol in loading_symbols:
        # 使用 \r 把光标移动到行首，再输出加载符号
        print(f'\rLoading {symbol}', end='', flush=True)
        # 暂停 1 秒钟
        time.sleep(0.3)
