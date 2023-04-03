# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/01/2023 22:23
# @Author  : Ctsuhlu 
# @File    : fabing.py

import random
from fabingdata import DATA
import time
import os

def fabing():
    msg = random.choice(DATA).format(target_name=target)
    print('\n' + msg)

def loading():
    print("\r加载中", end="")
    for i in range(3):
        print(".", end='', flush=True)
        time.sleep(0.3)

def get_target_name():
    global target
    count = 0
    target = str(input("请输入发病对象："))
    while True:
        if target.strip() == '':
            if count == 0:
                input("你没有输入发病对象，请重新输入：")
                count = count + 1
            elif count == 2:
                input("你是不是不想发病了:")
                count = count + 1
            else:
                print("哼，不管你了,拜拜(* ￣︿￣)")
                time.sleep(1)
                exit()
        else:
            return target

def ask_continue():
    choice = input('\n要继续发病吗？(按回车继续，输入q退出)')
    if choice == 'q':
        exit()

def clear():
    os.system('cls')

def main():
    get_target_name()
    clear()
    while True:
        loading()
        clear()
        fabing()
        ask_continue()
        clear()

if __name__ == '__main__':
    main()
