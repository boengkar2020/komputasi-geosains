#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:33:11 2022

@author: sukarno
"""

import sys, os

#add local libary path
sys.path.append(os.path.dirname(__file__))

from myarray.array import MyArray


if __name__ == '__main__':
    test1 = MyArray(data=[[2,3,9],[3,4,2],[7,5,3]])
    test2 = MyArray(data=[[5,4],[8,7]])
    
    print(test1)
    print("\n")
    print(test2)
    print("\n")