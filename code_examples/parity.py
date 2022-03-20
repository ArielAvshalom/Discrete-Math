#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:13:34 2022

@author: arielavshalom
"""
def add_1_and_check_parity(n):
    if (n+1) % 2 == 0:
        return n+1, "even"
    else:
        return n+1, "odd"
    
a = add_1_and_check_parity(6)