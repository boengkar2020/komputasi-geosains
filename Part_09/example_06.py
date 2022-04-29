#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:38:55 2022

@author: sukarno
"""

####################################################
# Deklarasi fungsi dengan default parameter
####################################################

def print_hello(nama = 'Agus'):

	print("Hello {}".format(nama))
    
if __name__ == '__main__' :
    
    #Panggil fungsi dengan default parameter
    #print_hello()
    
    #Panggil fungsi dengan parameter
    print_hello('Erlangga')