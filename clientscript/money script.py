#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 05:27:04 2018
  ________         __  ___          
 /_  __/ /_  ___  / / / (_)   _____ 
  / / / __ \/ _ \/ /_/ / / | / / _ \ 
 / / / / / /  __/ __  / /| |/ /  __/
/_/ /_/ /_/\___/_/ /_/_/ |___/\___/ 
             monetize your PC 

@author: kyr_n



### TODO: Convert this to an object on the main client script ###
### TODO: Fix the third output (e.g. 0.07500000000000001)

"""
import time

'''---------------
    MONEY COUNTER
   ---------------'''

tier = 2 ### TODO: Find a way of parsing the tier from main client script ###

if tier == 1:
    multiplyer = 0.05
elif tier == 2:
    multiplyer = 0.025
elif tier == 3:
    multiplyer = 0.005
else:
    multiplyer = 0.0005


p = 0

while True:
    interval = 60
    start = int(round(time.time()))
    while True:
        if int(round(time.time())) - start == interval:
            p += multiplyer
            break
    print(p)