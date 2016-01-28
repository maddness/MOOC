# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:22:29 2016

@author: aostrikov
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:02:17 2016

@author: aostrikov
"""

import sys

last_key = None

for line in open('input_average_time_comb.txt'):
    key = line.split()[0]
    
    if last_key == None and key:
        last_key = key  
        
    # different key        
    if key and last_key != key:
        print(last_key)
        last_key = key

if last_key:        
    print(last_key)