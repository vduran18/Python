#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:15:31 2019

@author: valeriaduran
"""
#Create the kinetic energy function 
def kinetic_energy(m,v):
    #The formula for kinetic energy
    kinenergy = 0.5 * m * v**2
    return kinenergy

#This is our main function for kinetic energy
def main():
        m = int(input("Enter mass in kilograms: "))
        v = int(input("Enter velocity in meters per second: "))
        if m >=0 and v >= 0: #Both values have to be positive 
            print("The object's kinetic energy is ", kinetic_energy(m,v))
        else:
            print("Enter a positive value.")
main()