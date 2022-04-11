#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:38:33 2022

@author: sukarno
"""

#Get semua key pada dictionary

D = { 'nama' : 'Yayan', 'umur' : 19, 'nilai' : [60,84,65]}

all_keys = D.keys()

print(all_keys)

for key in all_keys:
    value = D[key]
    print("{0} -> {1}".format(key,value))