#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:56:53 2022

@author: sukarno
"""

# Recursive function

def fib(n):
    
    if n == 0 or n == 1:
        return  1
    else:
        return (fib(n - 1) + fib(n - 2))
    
if __name__ == '__main__':
    n = int(input("Masukan nilai n : "))
    
    for i in range(0,n):
        print("{}".format(fib(i)))
        
        