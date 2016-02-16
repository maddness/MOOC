# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:40:01 2016

@author: aostrikov
"""
import sys

(last_key, last_number) = None, None

count = 0
tf_doc_num = []

for row in open('input.txt'):
    key, numbers = row.split('\t')
        
    (number, tf, i) = numbers.split(';')
    
    if last_key == None: 
        last_key = key        
        last_number = number
        
    if last_key == key:
        count += 1
        tf_doc_num.append((tf, number))
                                
    if last_key != key:
        for tf_val in tf_doc_num:
            print('{}#{}\t{}\t{}'.format(last_key, tf_val[1], tf_val[0], len(tf_doc_num)))
        
        count = 1
        last_key = key                
        last_number = number
        tf_doc_num = []
        tf_doc_num.append((tf, number))
                          
    
if last_key != None:
    for tf_val in tf_doc_num:
            print('{}#{}\t{}\t{}'.format(last_key, tf_val[1], tf_val[0], len(tf_doc_num)))