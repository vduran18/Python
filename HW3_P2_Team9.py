#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:59:09 2019

@author: valeriaduran
"""
#friends code that works
with open("steps.txt","r") as inputFile:
    lines = inputFile.readlines()
steps = list(map(int,lines))
daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]

print('{0:7s}\t{1:10s}\t{2:6s}\t{3:7s}'.format("Month", "Average", "Minimum", "Maximum"))
print('='*39)
start_month = 0
end_month = 0
# Loop through each month and do the calculations
for i, d in enumerate(daysInMonths):
    end_month += d
    steps_range = steps[start_month:end_month]
    avg_steps = (sum(steps_range))/d
    min_steps = min(steps_range)
    max_steps = max(steps_range)
    print('{0:2d}\t{1:7.3f}\t{2:4d}\t{3:5d}'.format(i+1, avg_steps, min_steps, max_steps))
    start_month += d
    
#MY code 

##Try again
inputFile = open("steps.txt", "r")  #reading the input file
outputFile = open("stepsfinal.txt", "w") #opens an output file to write result
outputFile.write("Month\t Average\t Minimum\t Maximum\n") #create header
print("Month\t Average\t Minimum\t Maximum\n")
#print("{:7s}\t{:7s}\t{:7s}\t{:7s}".format("Month", "Average", "Minimum", "Maximum"))
#print('='*39)
lines = inputFile.readlines() #reads lines from inputfile and stores as list
steps = list(map(int,lines)) #changes from string to numbers
daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
months = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sep", "Oct",
          "Nov", "Dec"]
start_month = 0
end_month = 0
#for d in enumerate(daysInMonths) :
    #end_month += d
    #steps_range = steps[start_month:end_month]
    #avg_steps = (sum(steps_range))/d
    #min_steps = min(steps_range)
    #max_steps = max(steps_range)
    #print("{:5s}\t{:7.3f}\t{:4d}\t{:5d}".format(months, avg_steps, min_steps, max_steps))
    #start_month += d
for x in range(0,12):
    end_month = start_month + daysInMonths[x] 
    steps_range = steps[start_month:end_month]
    avg_steps = float(sum(steps_range))/ max(len(steps_range),1)
    min_steps = min(steps_range)
    max_steps = max(steps_range)
    outputFile.write(months[x] + "{1:7.3f}\t".format(avg_steps) + "{2:4}\t".format(min_steps) + "{3:5}\t".format(max_steps))
    print(months[x] + "{1:7.3f}\t".format(avg_steps) + "{2:4}\t".format(min_steps) + "{3:5}\t".format(max_steps)) #tuple index out of range
    start_month = end_month
    
inputFile.close()
outputFile.close()
