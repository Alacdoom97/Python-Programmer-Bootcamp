# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:08:09 2020

@author: Pranav
"""


def TwoSum(num_list, target):
    
    d = {}
    
    for i in range(len(num_list)):
        if target - num_list[i] in d:
            d[num_list[i]] = i
            print(d)
            return [d[target-num_list[i]], i]
        else:
            d[num_list[i]] = i
    
    return -1
    