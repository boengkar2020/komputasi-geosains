#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:54:18 2022

@author: sukarno
"""

print("Program Start")

X = {'nama': 'John', 'nilai': 54}

if 'nama' in X:
	print("nama = {}".format(X['nama']))
else:
	print("Key tidak ditemukan")

print("Program Stop")