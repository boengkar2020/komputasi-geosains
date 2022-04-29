#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:22:48 2022

@author: sukarno
"""

###########################################
# Deklarasi fungsi dengan parameter input
# dan tanpa mengembalikan nilai
###########################################

def print_hello(nama):

    print("Hello {}".format(nama))
    
if __name__  == '__main__':
    #Panggil fungsi dengan parameter input
    print_hello("Anita")