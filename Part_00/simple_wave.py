#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:32:18 2022

@author: sukarno
"""

import matplotlib.pyplot as plt
import math

x_label = 'time (s)'
y_label = 'voltage (mv)'
chart_title = 'Simple sinus wave'

def nrange (min, max, delta = 1):
    last_data = min
    data = [last_data]
    
    while last_data <= max:
        last_data += delta
        data.append(last_data)
        
    return data


def f(A,t,freq):
    return A * math.cos(2 * math.pi * t * freq)


if __name__ == '__main__':
    A = float(input("Masukan amplitudo (mv) : "))
    freq = float(input("Masukan frequensi (Hz) : "))
    
    dt = 1 / (100 * freq)
    
    x = nrange(0.0, 1.0,dt)
    
    y = [f(A,t,freq) for t in x]

    fig, ax = plt.subplots()
    
    ax.plot(x, y)

    ax.set(xlabel=x_label, ylabel=y_label,
           title=chart_title)
    
    ax.grid()

    plt.show()