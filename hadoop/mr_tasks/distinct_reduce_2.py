# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:43:20 2016

@author: aostrikov
"""

import sys

last_val = None

groups = set()
result = {}

for line in open('input.txt'):      
    (val, group) = line.split()    
    
    if last_val == None and val:
        last_val = val  
    
    # same key
    if last_val == val:          
        groups.add(group)
        
    # different key        
    if last_val != val:                                
        for g in groups:                        
            if g in result:
                result[g] += 1
            else:
                result[g] = 1  
                
        last_val = val
        groups = set()
        groups.add(group)

for g in groups:                        
    if g in result:
        result[g] += 1
    else:
        result[g] = 1

if last_val: 
    for k, v in result.items(): 
        print(k + '\t' + str(v))