# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:08:22 2020

@author: Pranav
"""
A = [3,2,1]
B = []
C = []
count = 0

# def TowerOfHanoi(n, rod_A, rod_C, rod_B):
#     if n == 1:
#         print('Move disk 1 from rod', rod_A, 'to rod', rod_C)
#         return
#     TowerOfHanoi(n-1, rod_A, rod_B, rod_C)
#     print('Move disk', n, 'from rod', rod_A, 'to rod', rod_C)
#     TowerOfHanoi(n-1, rod_B, rod_C, rod_A)
    
def towers_of_hanoi(n, A, B, C):
    global count
    
    if n == 1:
        disk = A.pop
        C.append(disk)
        count +=1
    else:
        towers_of_hanoi(n-1, A, C, B)
        towers_of_hanoi(1, A, B, C)
        towers_of_hanoi(n-1, B, A, C)
    return count
    