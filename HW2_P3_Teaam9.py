#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:30:25 2019

@author: valeriaduran
"""


def get_input(w,h):
    try:
        w = int(input("Enter weight in pounds: "))
        h = int(input("Enter height in inches: "))
    except:
        print("Enter numbers only.")
    else:
        if w >= 0 and h >= 0:
            pass
            return w,h
        else: 
            print("Enter a positive value.")
    return None, None


#create bmi function
def calculate_bmi(w,h):
#the formula for bmi
   bmi = w * 703 / h**2
   return bmi

def calculate_weight_category(bmi):
    if bmi < 18.5:
        print("You are underweight")
    elif bmi > 25:
        print("You are overweight")
    else:
        print("You are at an optimal weight")


while True:
    w = int(input("Enter weight in pounds: "))
    h = int(input("Enter height in inches: "))
    we,he = get_input(w,h)
    if we is not None and he is not None:
        break
#Calculate and print BMI
bmi = calculate_bmi(we,he)
calculate_weight_category(bmi)
print(calculate_weight_category(bmi))