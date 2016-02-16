# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:40:01 2016

@author: aostrikov
"""
import sys

(last_key, last_doc_name, last_word) = None, None, None
count = 0

for row in open('input.txt'):
    key = row.split()[0]
        
    (word, doc_name) = key.split('#')
    
    if last_key == None: 
        last_key = key
        last_doc_name = doc_name
        last_word = word
    
    
    if last_key == key:
        count += 1
                
                
    if last_key != key:
        print('{}\t{}\t{}'.format(last_word, last_doc_name, str(count)))
        
        count = 1
        last_key = key                
        last_doc_name = doc_name
        last_word = word
                          
    
if last_key != None:
    print('{}\t{}\t{}'.format(word, doc_name, str(count)))
    