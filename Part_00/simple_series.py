#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:53:13 2022

@author: sukarno
"""

def nrange (min, max, delta = 1):
    last_data = min
    data = [last_data]
    
    while last_data <= max:
        last_data += delta
        data.append(last_data)
        
    return data

def f(n):
    return 4 + ((n -1) * 5)
    
if __name__ == '__main__':
    N = int(input('Masukan maksimum dari N : '))
    
    x = nrange(1,N)
    y = [f(n) for n in x]
    
    sn = ', '.join([str(c) for c in y])
    
    print('Sn : ' + sn)