# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 20:34:31 2016

@author: HOME
"""

# this function will take input from the user
# it will prompt using the str1 that has been passed to it
# finally it returs the user's input back to the parent class
def read_from_user(str1):
    input_1 = raw_input(str1)
    return input_1
    
if __name__== '__main__':
    # storing the users data into the input_main variable
    input_main = read_from_user('testing input prompt: ')
    
    print ("from main :", input_main)
    
    