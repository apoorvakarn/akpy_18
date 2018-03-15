# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:12:24 2018 by Apoorva Karn """
strs = 'abcdefghijklmnopqrstuvwxyz'       
def shifttext(shift):
    inp = raw_input('Input text here: ')
    data = []
    for i in inp:                     
        if i.strip() and i in strs:                  
            data.append(strs[(strs.index(i) + shift) % 26])    
        else:
            data.append(i)           
    output = ''.join(data)
    return output