#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:58:27 2022

@author: sukarno
"""

##############################
# Turunan dari object
##############################

class Person:

    fullname = ''

    def __init__ (self,nama):
        self.fullname = nama

    def speak(self):
        print('My Name is : {}'.format(self.fullname))
    
    def umur(self):
        pass

    def __str__ (self):
        return 'class Person <{}>'.format(self.fullname)
    
class Adult (Person):
	
    age = 20
	
    def __init__ (self,nama,age):
        super().__init__(nama)
        self.age = age

    def umur(self):
        print ("My Age is : {}".format(self.age))
        
    def drive_car(self):
        print('I can drive car')
        
        
class Kid (Person):
	
    age = 5
	
    def __init__ (self,nama,age):
        super().__init__(nama)
        self.age = age

    def umur(self):
        print ("My Age is : {}".format(self.age))
        
    def drive_bicycle(self):
        print('I can drive bicycle')
        
        
if __name__ == '__main__':
    # Deklarasi
    Jim = Kid ('Jimmy',6)
    Johny = Adult ('Johny',25)
    
    #Panggil method
    #Johny.drive_car()
    #Jim.umur()
    
    #Property
    #Johny.fullname = 'Johny Deep'
    #Johny.speak()
    Jim.age = 8
    Jim.umur()
    
    
    
    