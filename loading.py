# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/01/2023 23:34
# @Author  : Ctsuhlu 
# @File    : loading.py

import time

while True:
    print("\rLoading", end="")
    for i in range(6):
        print(".", end='', flush=True)
        time.sleep(0.3)
