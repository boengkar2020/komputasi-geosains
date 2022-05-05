#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:11:42 2022

@author: sukarno
"""

from myarray.array import MyArray

def zerro_matrix(row,col):
    return MyArray(row,col)

def diagonal_matrix(diag_val=[]):
    assert diag_val, 'value untuk diagonal harus diisi'
    
    l =  len (diag_val)
    
    mtx = MyArray(l,l)
    
    idx = 0
    for v in diag_val:
        mtx.matrix [idx][idx] = float(v)
        idx = idx + 1
        
    return mtx