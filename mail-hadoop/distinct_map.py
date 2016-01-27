# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:58:59 2016

@author: aostrikov
"""

import sys

for line in open('input.txt'):
    (value, groups_raw) = line.split()
    
    for group in groups_raw.split(','):        
        print('{},{}\t1'.format(value, group))