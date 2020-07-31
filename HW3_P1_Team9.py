#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:58:24 2019

@author: valeriaduran
"""

import re
#create a program to enter a tweet string
tweet = input("Enter tweet here: ")
word_count_twt = len(re.findall(r'\w+', tweet)) #counts number of words


#write a function that will count words while filtering out puncuation 
def word_count(tweet):
    word_count_twt = len(re.findall(r'\w+', tweet))
    print("The word count is: ", word_count_twt)
word_count(tweet)

#write a function that calculates avg number of characters
def ch_count(tweet):
    total = 0 #assign a variable starting at 0 
    for i in tweet:
        total = total + 1 #will give total # of characters
    avg_ch = total / word_count_twt #will give the avg character count
    print("Average character count is: ", avg_ch)
ch_count(tweet) 

#write a function that counts upper case letters
def up_case(tweet):
    count = 0
    for letter in tweet:
        if letter.isupper() :
            count = count + 1
    print("Upper case letters: ", count)
up_case(tweet)

#write a function that counts lowercase letters
def low_case(tweet):
    count = 0
    for letter in tweet:
        if letter.islower() :
            count = count + 1
    print("Lower case letters: ", count)
low_case(tweet)

#reverse the string
def rev_tweet(tweet):
    str = ""
    for i in tweet:
        str = i + str
    return str
rev_tweet(tweet)

#function for string stats
def tweet_stats(tweet):
    alphabets = digits = special = 0 #assign variables to hold count and must begin at 0
    for i in range(len(tweet)) :
        if tweet[i].isalpha() : #if an alphabet, count
            alphabets = alphabets + 1
        elif(tweet[i].isdigit()) : #if a number, count
            digits = digits + 1
        else:
            special = special + 1 #if nothing else, count as a special character
    print("Total number of alphabets is: ", alphabets)
    print("Total number of digits is: ", digits)
    print("Total number of special characters is: ", special)
tweet_stats(tweet)