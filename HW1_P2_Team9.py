#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 08:24:37 2019

@author: valeriaduran
"""

#Calculating Balance of Account

#num1 represents P the principal amount
num1 = int(input("Enter amount of P: "))

#num2 represents r the annual interest rate
num2 = float(input("Enter annual interest rate: "))

#num3 represents n the numeber of times per year interest is compunded
num3 = int(input("Enter number of times interest is compunded: "))

#num4 represents t the specified number of years
num4 = int(input("Enter number of years: "))

#money represents A the amount of money in the account 
money = num1 * (1 + (num2/num3))**(num3 * num4) 

#Display amount of money in the account after specified years
print("A = ", money)