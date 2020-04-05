# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:41:48 2020

@author: Pranav
"""

# def card_validation():
#     card_num = input('please enter credit card number: ')
#     number_list = [int(char) for char in card_num]
#     number_length = len(number_list)
#     number_reverse = number_list[::-1]
#     print('number list:', number_list)
#     print('number list reverse:', number_reverse)
#     double = 0
#     single = 0
    
#     for i in range(0, number_length):
#         if i % 2 != 0:
#             if 2*number_reverse[i] > 9:
#                 double = double + 2*number_reverse[i] - 9
#             else:
#                 double = double + 2*number_reverse[i]
#         else:
#             single = single + number_reverse[i]
            
#     if (double + single) % 10 == 0:
#         print(card_num, 'is a valid credit card number')
#     else:
#         print(card_num, 'is not a valid credit card number')

def thousand_coins():
    number_of_coins = 1001
    # Note: 0 means heads, 1 means tails.
    # append 1000 values in the list, each being 0 for heads
    coins_list = [0]*number_of_coins

    for jump in range(1,number_of_coins):
        for j in range(0, number_of_coins, jump):
            # if the value is 0 it will turn to 1, if it's 1, it will turn to 0
              coins_list[j] = 1 - coins_list[j]
    
    d = {}
    for i,v in enumerate(coins_list):
        if v != 0:
            d[i] = v
    
    print(d)