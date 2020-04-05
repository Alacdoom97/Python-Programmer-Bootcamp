# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:45:50 2020

@author: Pranav
"""

import sys
import multiprocessing as mp

list_numbers = [1,3,4,5]

# Question 1
# Can you write a short program that will print out the version of Python
# that you are using?

# print(sys.version)

# Question 2
# Write a program that requests five names separated by commas and create a
# list containing those names. Print your answer.
# For example James,Alison,Fred,Sally,Matthew
# should return ['James','Alison','Fred','Sally','Matthew']

# names = input('Please input 5 names seperated by commas: ')
# list_names = names.split(',')
# print(list_names)

# Question 3
# Write a program to determine whether a given number is within 10 of 100 or 200.

# def check_number(number):
#     if(abs(100-number)) <= 10 or (abs(200-number)) <=10:
#         return True
#     else:
#         return False

# Question 4
# Write a program that takes a list of non-negative integers and prints each integer
# to the screen the same number of times as the value of the integer, each new value
# on a new line. For example
# [2,3,4,1] would print:
# 22
# 333
# 4444
# 1

# def print_number(numlist):
#     for i in numlist:
#         if i < 0:
#             error_message = 'There is a negative number in the list. Shutting down'
#             sys.exit(error_message)
    
#     for number in numlist:
#         number_name = ''
#         for i in range(number):
#             number_name = number_name + str(number) + ''
#         print(number_name)

# Question 5
# Write some code that will return the number of CPUs in the system.

# print('Number of CPU\'s:', mp.cpu_count())

# Question 6
# Write a program that will return the sum of the digits of an integer.

# def sum_finder(num):
#     num = str(num)
#     total = 0
#     for i in num:
#         print(i)
#         i = int(i)
#         total = total + i
#     return total

# Question 7
# Write a program that converts text into pig latin. Pig latin works as follows:
# All letters before initial vowel are placed at the end of the word and then 'ay'
# is added (explanation adapted from Wikipedia), so pig becomes igpay, cat becomes
# atcay, potential becomes otentialpay etc.

# def pig_latin(word):
#     vowels = ['a','e','i','o','u']
#     front = None
#     for index, char in enumerate(word):
#         if char in vowels:
#             front = word[index:]
#             back = word[:index]
#             break
#     if not front:
#         return 'No vowels!'
#     translation = front + back + 'ay'
#     return translation

# Question 8
# Write a function that will check for the occurrence of double letters in
# a string. If the string contains double letters next to each other it
# will return True, otherwise it will return False.

# def double(string):
#     str_len = len(string)
#     for i in range(str_len - 1):
#         if string[i] == string[i+1]:
#             return True

#     return False

# Question 9
# Write a function that will check if a string is a palindrome.

# def palindrome(string):
#     string = str(string)
    
#     for i in range(len(string)):
#         if string[i] != string[-1-i]:
#             return False
#     return True

# Question 10
# Write a function def add_commas(numbers) that will add commas to an integer and return it as a string.
# For example add_commas(1000000) will return 1,000,000 Do it first without using string fomratting
# or f strings.

# def add_commas(number):

#     str_number = str(number)

#     str_number = str_number[::-1]
#     comma = ','
#     new_str = ''
#     for i, num in enumerate(str_number):
#         if i != 0 and (i % 3) == 0:
#             new_str = new_str + comma
#         new_str = new_str + num

#     return new_str[::-1]






