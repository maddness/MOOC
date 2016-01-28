# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:02:17 2016

@author: aostrikov
"""

import sys
import re

(last_url, all_time, all_count) = (None, 0, 0)

for line in open('input_average_time_comb.txt'):
    match = re.search(r'(\S+)\t(\d+);(\d+)', line)
    
    if match:
        (url, time, count) = (match.group(1), int(match.group(2)), int(match.group(3)))
 
    if last_url == None and url:
        last_url = url
        
    # same key
    if url and last_url == url:
        all_time += time
        all_count += count      
        
    # different key        
    if url and last_url != url:
        print(last_url + '\t' + str(all_time) + ';' + str(all_count))
        (last_url, all_time, all_count) = (url, time, count)        

if last_url:        
    print(last_url + '\t' + str(all_time) + ';' + str(all_count))