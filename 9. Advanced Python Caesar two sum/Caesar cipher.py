# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:01:54 2020

@author: Pranav
"""


def encrypt(text, number):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_msg = ''
    
    if number < 0:
        print('Error, number cannot be lower than 0')
    if number > 25:
        number = number % 25
        print(f'number after modulo: {number}')
    
    text = text.lower()
    print(f'Text with lower case: {text}')
    
    for char in text:
        if char not in alphabet_list:
                new_letter = char
                encrypted_msg = encrypted_msg + new_letter + ''
        for alpha in alphabet_list:
                encryption_number = alphabet_list.index(alpha) + number
                if encryption_number > 25:
                    encryption_number = encryption_number % 26
                if char is alpha:
                    new_letter = alphabet_list[encryption_number]
                    encrypted_msg = encrypted_msg + new_letter + ''
    
    encrypted_msg.capitalize()
    print('Encrypted message:', encrypted_msg)
    
def decrypt(text, number):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decrypted_msg = ''
    
    if number < -26:
        number = number % -25
        print(f'number after modulo: {number}')
    
    text = text.lower()
    print(f'Text with lower case: {text}')
    
    for char in text:
        if char not in alphabet_list:
                new_letter = char
                decrypted_msg = decrypted_msg + new_letter + ''
        for alpha in alphabet_list:
                if char is alpha:
                    decryption_number = alphabet_list.index(alpha) + number
                    new_letter = alphabet_list[decryption_number]
                    decrypted_msg = decrypted_msg + new_letter + ''
    
    decrypted_msg.capitalize()
    print('Decrypted message:', decrypted_msg)