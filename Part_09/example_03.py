#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:23:17 2022

@author: sukarno
"""

###############################################
# Deklarasi fungsi dengan mengembalikan nilai
###############################################

def print_hello(nama):

	return "Hello {}".format(nama)

if __name__ == '__main__' :
    #panggil fungsi
    mahasiswa = print_hello("Hendro!!")
    
    print(mahasiswa)
    
