# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:11:49 2020

@author: Pranav
"""

# -------------------------------------------------------------------------
# Constant Time - O(1) runs at a constant time regardless of input data (n)
# -------------------------------------------------------------------------

# a,b = 2,4

# if a > b:
#     print(True)
# else:
#     print(False)
    
# --------------------------------------------------------------------------------------
# Logarithmic Time O(log n) reduces the size of the input data in each step.
# A good example of popular logarithmic time complexity operation is binary search trees
# as shown below.
# --------------------------------------------------------------------------------------
    
# def binary_search(data, value):
#     n = len(data)
#     left = 0
#     right = n - 1
#     while left <= right:
#         middle = (left + right) // 2
#         if value < data[middle]:
#             right = middle - 1
#         elif value > data[middle]:
#             left = middle + 1
#         else:
#             return middle
#     raise ValueError('Value is not in the list')
    
# if __name__ == '__main__':
#     data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(binary_search(data, 8))

# ----------------------------------------------------------- 
# Linear Time - O(n) inceases linearly as input data increase
# -----------------------------------------------------------
    
# data = range(1,35,1)

# for value in data:
#     print(value)
   
# ----------------------------------------------------------------------------
# Quadratic Time - O(n^2) occurs when each input needs a linear time operation
# ----------------------------------------------------------------------------

# data = range(20)

# for x in data:
#     for y in data:
#         print(x, y)

# ----------------------------------------------------------------------------
# Exponential Time - O(2^n) occurs when the growth doubles with each addition 
# to the input data set. Usually this is seen in brute-force algorithms like
# below.
# ----------------------------------------------------------------------------

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
