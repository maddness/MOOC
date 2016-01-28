# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:46:19 2016

@author: aostrikov
"""
import sys

(last_url, all_time, count) = (None, 0, 0)

for line in open('input_average_time.txt'):
    (url, time) = line.split()
    
    if last_url == None and url:
        last_url = url
        
    # same key
    if url and last_url == url:
        all_time += int(time)
        count += 1      
        
    # different key        
    if url and last_url != url:
        print(last_url + '\t' + str(float(all_time/count)))
        (last_url, all_time, count) = (url, int(time), 1)        

if last_url:        
    print(last_url + '\t' + str(float(all_time/count)))
        
        