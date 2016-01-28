# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:26:55 2016

@author: aostrikov
"""

import sys

for line in open('input.txt'):
    words = {}
    for word in line.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    for k, v in words.iteritems():
        print(k + '\t' + str(v))
