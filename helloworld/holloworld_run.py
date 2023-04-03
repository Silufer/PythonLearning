# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 04/01/2023 23:24
# @Author  : Ctsuhlu 
# @File    : holloworld_run.py

import helloworld
import random
for t in range(random.randint(0, 50)):
    print(str(t + 1) + '.', end='')
    helloworld.print_helloworld()
