#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:08:42 2022

@author: arielavshalom
"""

P, Q, R = 1,1,1

def give_input():
    
    P = int(input('enter P \n'))
    Q = int(input('enter Q \n'))
    R = int(input('enter R \n'))
    
    return [P, Q, R]


def tester(list_of_bools):
    
    print("P^Q^R")
    
    if list_of_bools[0] and list_of_bools[1] and list_of_bools[2]:
        print('Yaaaas')
    else:
        print('boo hoo')
        
def implication_tester_RandQ_implies_P(list_of_bools):
    
    print("R^Q => P")
    print(f"{list_of_bools[2]}^{list_of_bools[1]}=>{list_of_bools[0]}")
    
    if list_of_bools[1] and list_of_bools[2]:
        if not list_of_bools[0]:
            print('False!')
        else:
            print("True! Both Q^R are true and so is => P")
    else:
        if not list_of_bools[0]:
            print("Implication true because both sides are False! This is Vacuously True")
        else:
            print("Vaculously True! This is because the antecedant is false, and the Consequent is true.")
        
if __name__ == "__main__":
    bool_list = give_input()
    
    tester(bool_list)
    print('\nNext Test\n')
    implication_tester_RandQ_implies_P(bool_list)