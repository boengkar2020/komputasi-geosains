#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:10:40 2022

@author: sukarno
"""

print("Menampilkan bilangan ganjil")

for i in range(0,100):
	if (i%2) == 0:
		continue
 
	print("No : {}".format(i))

print("---- SELESAI -----")