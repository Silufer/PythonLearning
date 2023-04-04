# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/04/2023 00:01
# @Author  : Ctsuhlu 
# @File    : loading3.py

import time
import _thread

def loading(lock):
    """等待函数"""
    chars = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 0
    while lock[0]:
        i = (i+1) % len(chars)
        print('\033[A%s %s' %
              (chars[i], lock[1] or '' if len(lock) >= 2 else ''))
        time.sleep(0.25)
    print('')

def long_task(lock):
    """模拟长时间任务"""
    for i in range(10):
        print('正在执行第 %s 步...' % i)
        time.sleep(1)

    # 任务完成，释放锁停止等待动画显示
    lock[0] = False


lock = [True]  # 控制等待动画的锁
_thread.start_new_thread(loading, (lock,))  # 开启等待动画线程

long_task(lock)  # 执行长时间任务

print('任务已完成！')
