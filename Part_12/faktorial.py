#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:28:33 2022

@author: sukarno
"""

# Recursive function

def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
if __name__ == '__main__':
    n = int(input("Masukan nilai n : "))
    res = factorial(n)
    print(f"{n}! adalah {res}")