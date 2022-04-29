#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:48:25 2022

@author: sukarno
"""

#######################################
# Deklarasi sebuah class untuk Object
#######################################

class Person:

	fullname = ''

	def __init__ (self,nama):
		self.fullname = nama

	def speak(self):
		print('My Name is : {}'.format(self.fullname))

	def __str__ (self):
		return 'class Person <{}>'.format(self.fullname)
    

if __name__ == '__main__' :
    #deklarasi instance dari object
    bob = Person('Bob')
    tom = Person('Tom')
    alice = Person('Alice')
    
    # Menggunakan object method
    #bob.speak()
    #tom.speak()
    #alice.speak()
    
    # Menggunakan object property
    #print(bob.fullname)
    bob.fullname = 'Bob Marley'
    print(bob.fullname)
    bob.speak()