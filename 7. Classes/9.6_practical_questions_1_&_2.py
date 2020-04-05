# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''
# class BankAccount(object):
#     ''' Bank Account '''
    
#     def __init__(self, balance=0.0):
#         self.balance = balance
    
#     def deposit(self):
#         amount = float(input('How much would you like to deposit? :>'))
#         self.balance = self.balance + amount
#         print(f'{amount} dollars deposited successfully!')
    
#     def withdraw(self):
#         amount = float(input('How much would you like to withdraw? :>'))
#         if amount > self.balance:
#             print(f'You do not have sufficient funds to withdraw, your balance is: {self.balance} dollars.')
#         else:
#             self.balance = self.balance - amount
#             print(f'{amount} dollars withdrawn!')
    
#     def displayAmount(self):
#         print(f'{self.balance} dollars in the account currently.')

'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''
# import math

# class Circle(object):
#     ''' Circle Maths '''
    
#     def __init__(self):
#         radius = float(input('What is the radius of the circle you want? :>'))
#         self.radius = radius
    
#     def calc_area(self):
#         area = math.pi * (self.radius)**2
#         return area
