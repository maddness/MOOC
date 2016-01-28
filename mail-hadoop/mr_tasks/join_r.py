# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 08:28:29 2016

@author: maddness
"""

import sys
import re


last_key, last_label, last_action = None, None, None

queries = []
urls = []

for line in open('input_join.txt'):
    match = re.search(r'(\S+)\t(\S+):(.+)', line)
    (key, label, action) = match.group(1), match.group(2), match.group(3)
    
    if last_key == None:
        last_key = key
        last_label = label
        last_action = action
    
    
    # same key    
    if last_key == key:
        if label == 'query': queries.append(action)
        if label == 'url': urls.append(action)
        
        
    # different key    
    if last_key != key:
        if len(queries) > 0 and len(urls) > 0:
            for q in queries:
                for u in urls:
                    print(last_key + '\t' + q + '\t' + u)
            
        last_key = key
        queries = []
        urls = []
        
        if label == 'query': queries.append(action)
        if label == 'url': urls.append(action)
    
  
if last_key != None and len(queries) > 0 and len(urls) > 0:
    for q in queries:
        for u in urls:
            print(last_key + '\t' + q + '\t' + u)    