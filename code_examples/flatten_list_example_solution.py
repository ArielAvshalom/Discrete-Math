#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:44:36 2022

@author: arielavshalom
"""
#expected input : [1,2,3,4,[5,6],[[7,8,9],[1,2,3]],10]
#expected output: [1,2,3,4,5,6,7,8,9,1,2,3,10]

def flatten_list(old_list, new_list = []):
    for element in old_list:
        if isinstance(element, list):
            
            
            print(f"the current element is a list and it is {element}")
                        
            flatten_list(element, new_list)

            
        else:
            new_list.append(element)
            
            print(f"the current element is NOT a list and it is {element}")
    
    return new_list

flattened_list = flatten_list([1,2,3,4,[5,6],[[7,8,9],[1,2,3]],10])