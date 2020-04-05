# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:23:05 2020

@author: Pranav
"""


class Card(object):
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value
        
    def __str__(self):
        card = str(self.value) + " of " + str(self.suit)
        return card
        