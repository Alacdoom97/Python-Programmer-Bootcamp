# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''
# capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#             'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#             'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#             'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
#             }

# user_in = input('Give a country name here please: ')
# count = 0

# user_in.capitalize()

# for country in capitals:
#     if country == user_in:
#         print(user_in, 'is in the dictionary and the capital is', capitals[user_in])
#         count = 1

# if count == 0:
#     print(user_in, 'is not in the dictionary. Sorry!')
    
'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''

# number_1 = 0
# number_2 = 1
# fib_dict = {}

# for i in range(1, 13, 1):
#     fib_dict[i] = number_1
#     number_1, number_2 = number_2, number_1 + number_2

# print(fib_dict)

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

# companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
# key_names = ['Open', 'High', 'Low', 'Close']
# prices = [[12.87, 13.23, 11.42, 13.10], [23.54,25.76,21.87,22.33],
#           [98.99,102.34,97.21,100.065], [203.63,207.54,202.43,205.24]]

# dict_1 = {}

# for i in range(len(key_names)):
#     dict_1[companies[i]] = dict(zip(key_names,prices[i]))

# print(dict_1)

'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''


'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
# import random
# import matplotlib.pyplot as plt

# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphadict = {}

# for letter in alphabet:
#     alphadict[letter] = random.randint(1, 100)

# print(alphadict)
# x,y = zip(*alphadict.items())
# plt.bar(x,y)

'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''

# suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
# card_numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9' '10', 'Jack', 'Queen', 'King']
# card_dict = dict()

# for i in suits:
#     card_dict[i] = card_numbers
    
# print(card_dict)