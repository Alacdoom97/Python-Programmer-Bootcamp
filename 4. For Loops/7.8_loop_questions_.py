#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
# number_1 = int(input('Insert a number between 1 - 100 here: '))
# number_2 = int(input('Insert a second number between 1 - 100 here: '))

# if number_1 < number_2:
#     for i in range(number_1, number_2 + 1, 1):
#         print(i, end=" ")
# elif number_2 < number_1:
#     for i in range(number_2, number_1 + 1, 1):
#         print(i, end=" ")
# else:
#     print(number_1)

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''

# text = str(input('Type anything you wish here: '))
# print(text)
# length = int(len(text))

# for i in range(length-1, -1, -1):
#     print(text[i], end="")

'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''

# number = input('Give a number between 1 and 12 please: ')

# while (not number.isdigit()) or (int(number) < 1 or int(number) > 12):
#     print('Must be an integer between 1 and 12!')
#     number = input('Please try again: ')

# number = int(number)
# for i in range(1, 11, 1):
#     print(number, 'x', i, '=', number*i)

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''

# for i in range(1, 11, 1):
#     for j in range(1, 13, 1):
#         if j == 12:
#             print(j, 'x', i, '=', j*j)
#         else:
#             print(j, 'x', i, '=', j*j, end="  ")

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

# user_input = int(input('Please insert a bunch och numbers and enter -1 when you want to stop. Start here: '))
# data= []

# while user_input != -1:
#     data.append(user_input)
#     print('Entry accepted!')
#     user_input = int(input('Next number please: '))
    
# mean = sum(data) / len(data)

# print('Numbers inserted:', data)
# print('Mean of the numbers given is:', mean)


'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
# total = 0

# for i in range(15, 0, -1):
#     if total == 0:
#         total = i
#     else:
#         total = total * i
        
# print(total)

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''

number_1 = 0
number_2 = 1
fib_number = 20
data = []

for i in range(fib_number):
    data.append(number_1)
    number_1, number_2 = number_2, number_1 + number_2

print(data)


'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''

# # Make a for loop which runs 6 times, the amount of times needed to make the F vertically
# for i in range(6):
#     # If the i variable is in the first iteration, then print 5 stars
#     if i == 0:
#         print('*****')
#     # If i is in the third iteration, then print 4 stars
#     elif i == 2:
#         print('****')
#     else: # Otherwise print only 1 star for the base line
#         print('*')



'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''

# list_odd = []
# list_even = []

# for i in range(101):
#     if i % 2 == 0:
#         list_even.append(i)
#     else:
#         list_odd.append(i)

# print(list_odd)
# print(list_even)