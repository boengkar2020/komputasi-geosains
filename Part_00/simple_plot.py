#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:34:33 2022

@author: sukarno
"""

import matplotlib.pyplot as plt

def nrange (min, max, delta = 1):
    last_data = min
    data = [last_data]
    
    while last_data < max:
        last_data += delta
        data.append(last_data)
        
    return data


def f(x) :
    return x

if __name__ == '__main__':
    
    dt = 1  #kecilkan nilainya jika grafik tidak bagus
    
    x = nrange(0, 10,dt)
    y = [f(i) for i in x]
    
    fig, ax = plt.subplots()
    
    ax.plot(x, y)
    
    ax.grid()

    plt.show()
    