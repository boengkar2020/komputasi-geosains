#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:37:33 2022

@author: sukarno
"""
MAX_ROW = 3
MAX_COL = 3


class MyArray(object):
    num_row = MAX_ROW
    num_col = MAX_COL
    matrix = []
    
    def __init__ (self,row = MAX_ROW, col = MAX_COL, data = []) :
        
        assert row <= MAX_ROW, f"row melebihi : {MAX_ROW}"
        assert col <= MAX_COL, f"col melebihi : {MAX_COL}"
        assert row > 0, "row harus di atas 0"
        assert col > 0, "col harus di atas 0"
        
        if not data:
            self.num_row = row
            self.num_col = col
            
            self.__build_array()
        
        else :
            self.num_row = len(data)
            self.num_col =len(data[0])
            
            assert len(data) <= MAX_ROW, f"Jumlah row melebihi : {MAX_ROW}"
            for d in data:
                assert len(d) <= MAX_COL, f"Jumlah row melebihi : {MAX_COL}"
                
            self.matrix = []
            
            for m in data:
                arr = []
                for n in m:
                    arr.append(float(n))
                    
                self.matrix.append(arr)
            
    def __build_array(self) :
        self.matrix = []
        
        for m in range(0,self.num_row):
            arr = []
            for n in range(0,self.num_col):
                arr.append(0.0)
                
            self.matrix.append(arr)
            
    def at(self,row,col):
        return self.matrix[row][col]
    
    def __str__ (self):
        s = [[str(e) for e in row] for row in self.matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)