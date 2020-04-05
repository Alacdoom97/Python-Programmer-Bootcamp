# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:15:24 2019

@author: giles
"""

# Exercises

'''
Question 1
Create a function that will calculate the sum of two numbers. Call it sum_two.
'''
# def sum_two(a,b):
#     return a + b

# print(sum_two(5,6))

'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''
# def multiply(a, number=2):
#     return a * number

# print(multiply(5,7))
# print(multiply(5))

'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''
# def power(a, power=2):
#     return a**power

# print(power(3,4))
# print(power(3))

'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''
# file = open('capitals.txt', 'w')
# file.write('New Delhi, Paris, Stockholm, Beijing, Tokyo')
# file.close()
# file = open('capitals.txt', 'r')
# print(file.read())
# file.close()

'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
'''
# user_input = input('State a capital city here: ')
# user_input = user_input.title()

# f = open('capitals.txt', 'a')
# f.write(', ' + user_input)
# print('Entry added successfully!')
# f.close()

# file = open('capitals.txt', 'r')

# print(file.read())

# file.close()


'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''
# file = open('file_1.txt', 'r')

# content = file.read()

# file2 = open('file_2.txt', 'w')

# file2.write(content)

# file2.close()

# f = open('file_2.txt', 'r')

# print(f.read())

