# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:20:04 2016

@author: aostrikov
"""
import sys

for row in open('input.txt'):    
    (word, doc_num, tf) = row.split('\t')    
    print('{}\t{};{};1'.format(word, doc_num, tf.replace('\n','')))
        
        