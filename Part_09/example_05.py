#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:33:43 2022

@author: sukarno
"""

####################################
# Penggunaan return
###################################

def jumlah (a,b):
	if a < 0:
		return

	if b < 0:
		return

	return a + b

if __name__ == '__main__':
    a = int(input("Masukan nilai a : "))
    b = int(input("Masukan nilai b : "))
    
    #Panggil fungsi jumlah
    hasil = jumlah(a, b)
    
    if hasil:
        print("Hasil a + b = {0}".format(hasil))
    else:
        print("Salah satu parameter lebih kecil dari 0")