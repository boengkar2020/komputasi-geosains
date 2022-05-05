#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 21:40:28 2022

@author: sukarno
"""

from myarray.array import MyArray

def add_matrix(arr1,arr2):
    assert arr1, 'array 1 harus diisi'
    assert arr2, 'array 2 harus diisi'
    
    assert isinstance(arr1, MyArray), 'arr1 tipe data harus MyArray'
    assert isinstance(arr2, MyArray), 'arr2 tipe data harus MyArray'
    
    assert arr1.num_row == arr2.num_row, 'arr1 dan arr2 berbeda ukuran row'
    assert arr1.num_col == arr2.num_col, 'arr1 dan arr2 berbeda ukuran col'
    
    result = MyArray(arr1.num_row,arr1.num_col)
    
    for m in range(0,arr1.num_row):
        for n in range(0,arr1.num_col):
            result.matrix [m][n] = float(arr1.at(m,n) + arr2.at(m,n))
            
    return result

def multiply_matrix(arr1,arr2):
    assert arr1, 'array 1 harus diisi'
    assert arr2, 'array 2 harus diisi'
    
    assert isinstance(arr1, MyArray), 'arr1 tipe data harus MyArray'
    assert isinstance(arr2, MyArray), 'arr2 tipe data harus MyArray'
    
    assert arr1.num_row == arr2.num_col, 'arr1 dan arr2 berbeda ukuran row'
    
    data = []
    
    for v in arr1.matrix:
        d = []
        for n in range(0,arr2.num_col):
            t = 0
            for m in range(0,arr2.num_row):
                t += float(v[m] * arr2.at(m,n))
                
            d.append(t)
        data.append(d)
                
    return MyArray(data=data)

def determinant_matrix(arr):
    assert arr, 'array harus diisi'
    assert isinstance(arr, MyArray), 'arr tipe data harus MyArray'
    assert arr.num_row == arr.num_col, 'tipe array harus square'
    
    if arr.num_row == 2:
        det = (arr.at(0,0) * arr.at(1,1)) - (arr.at(1,0) * arr.at(0,1))
    elif arr.num_row == 3:
        det = arr.at(0,0) * determinant_matrix(MyArray(data=[[arr.at(1,1),arr.at(1,2)],[arr.at(2,1),arr.at(2,2)]]))
        det -= arr.at(0,1) * determinant_matrix(MyArray(data=[[arr.at(1,0),arr.at(1,2)],[arr.at(2,0),arr.at(2,2)]]))
        det += arr.at(0,2) * determinant_matrix(MyArray(data=[[arr.at(1,0),arr.at(1,1)],[arr.at(2,0),arr.at(2,1)]]))
    else:
        det = arr.matrix[0]
        
    return det

def transpose_matrix(arr):
    assert arr, 'array harus diisi'
    assert isinstance(arr, MyArray), 'arr tipe data harus MyArray'
    
    data = []
    
    for val in arr.matrix:
        if not data:
            for v in val:
                data.append([v])
                
        else:
            m = 0
            for v in val:
                data[m].append(v)
                m += 1
                
    return MyArray(data=data)