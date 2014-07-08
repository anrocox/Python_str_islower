#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2014

@author: anroco

In a python str how to know if characters are lowercase?

En un str python ¿como saber si todos los caracteres son minusculas?
'''

#create a str
s = 'textual data in python'
print(s)

#the islower() method verify if all characters in the string are lowercase.
#return True or False
print(s.islower())

#create a str
s = 'Textual data in Python'
print(s)

#return False because exists several character in uppercase
print(s.islower())
