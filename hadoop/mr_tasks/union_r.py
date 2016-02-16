# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 08:28:29 2016

@author: maddness
"""

import sys

(last_key, last_label, count) = (None, None, 0)

for line in open('input.txt'):
    (key, label) = line.split()
    
    if last_key == None: (last_key, last_label) = (key, label)
        
    if last_key == key:
        count += 1
        
    if last_key != key:
        if count == 1 and (last_label == 'A' or last_label == 'B'): 
            print(last_key)
            
        last_key = key
        count = 1
        
    last_label = label
        
  
if last_key != None and count == 1 and (last_label == 'A' or last_label == 'B'):
        print(last_key)    