#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:12:23 2022

@author: sukarno
"""

import random

print("---- Program tebak angka ---- \n")

Angka = random.randint(0,1000)

while True:
	ch = input("Masukan angka dari 0 – 1000 :")

	if not ch.isalnum():
		print("Yang anda masukan bukan angka")
		continue

	ch = int(ch)
	
	if ch == Angka:
		print("Tebakan anda benar")
		break
	elif ch < Angka:
		print("Tebakan anda terlalu kecil")
	elif ch > Angka:
		print("Tebakan anda terlalu besar")

print("----- Selesai ------")