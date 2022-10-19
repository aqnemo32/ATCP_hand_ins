#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 11:56:29 2022

@author: achilequarante
"""
list_ = []
f = open('ucope_1_1.csv')
f.readline()
f.readline()

for i in f:
    list_.append(i.readline.split(','))
                
print(list_)    
