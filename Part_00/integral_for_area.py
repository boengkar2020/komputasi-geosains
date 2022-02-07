#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:57:01 2022

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
    return x*x


def integral(f,x,dx):
    area = 0
    
    for i in x:
        area += f(i) *dx
        
    return area


if __name__ == '__main__':
    
    dx = 0.001  #kecilkan nilainya jika grafik tidak bagus
    
    min = int(input("Batas bawah : "))
    max = int(input("Batas atas : "))
    
    x = nrange(min, max,dx)
    y = [f(i) for i in x]
    
    area = integral(f,x,dx)
    
    print('Luas area di bawah kurva : {0}'.format(area))
    
    fig, ax = plt.subplots()
    
    ax.plot(x, y)
    
    ax.grid()

    plt.show()
    