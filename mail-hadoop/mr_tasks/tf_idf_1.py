# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:20:04 2016

@author: aostrikov
"""
import sys
import re

for row in open('input.txt'):
    match = re.search(r'(\S+?):(.+)', row)
    (name, line) = match.group(1), match.group(2)
    for word in re.findall(r'\w+', line):
        print('{}#{}\t1'.format(word, name))
        
        