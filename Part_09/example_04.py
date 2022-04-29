#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:23:41 2022

@author: sukarno
"""

###########################################################
# Deklarasi fungsi dengan parameter input lebih dari satu
###########################################################

def jumlah (a,b):
	result = a + b
	return result

if __name__ == '__main__' :
    a = int(input("Masukan nilai a : "))
    b = int(input("Masukan nilai b : "))
    
    #Panggil fungsi jumlah
    hasil = jumlah(a, b)
    
    print("Hasil a + b = {0}".format(hasil))