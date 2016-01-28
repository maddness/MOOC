# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:25:36 2016

@author: maddness
"""

import sys

def print_map(pairs):
    lollis = []
    for k, v in pairs.items():
        lollis.append(k + ':' + str(v))
        
    return ','.join(lollis)
    

for line in open('input_1.txt'):
    tokens = line.split()  
    sent_tokens = set()     
    
    for i, main_token in enumerate(tokens):
        if main_token in sent_tokens: 
            continue        
        else:
            sent_tokens.add(main_token)
            
        repeat_factor = 1
        counts = {}
        
        for j, second_token in enumerate(tokens):
            if main_token == second_token and i != j:  
                repeat_factor += 1
            if main_token != second_token:
                if second_token in counts:
                    counts[second_token] += 1
                else:
                    counts[second_token] = 1
        
        result = { k: v * repeat_factor  for (k, v) in counts.items() }
        print(main_token + '\t' + print_map(result))