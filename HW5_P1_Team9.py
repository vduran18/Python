#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:56:33 2019

@author: valeriaduran
"""

import numpy as np
fname = 'insurance.txt' #name the file 
dtype1 = np.dtype([('age', np.int), ('sex', '|S6'), ('bmi', np.float), 
                   ('children', np.int), ('smoker', '|S3'), ('region', '|S9'),
                   ('expenses', np.float)]) #fix code in order to read strings and ints
np.loadtxt(fname, dtype1, skiprows=1) #load the txt file skipping the header row
a = np.loadtxt(fname, dtype1, skiprows=1) #save the adjusted txt file 
#find mean, sd, and median of age
mn_age = a['age'].mean()
mn_age
# the mean age is 39.20702541106129
sd_age = a['age'].std()
sd_age
# the standard deviation for age is 14.044709038954522
med_age = np.median(a['age'])
med_age
#the median age is 39.0

#find mean, sd, and median of bmi
mn_bmi = a['bmi'].mean()
mn_bmi
# the mean bmi is 30.66547085201794
sd_bmi = a['bmi'].std()
sd_bmi
# the standard deviation for age is 6.096102846926171
med_bmi = np.median(a['bmi'])
med_bmi
#the median age is 30.4

#find mean, sd, and median of bmi grouped by sex
##MALES

male = a['sex'] == b'male'
m_mn = a['bmi'][male].mean() #Find the mean bmi of males
m_mn #mean bmi for males is 30.94526627218935

m_sd = a['bmi'][male].std() #Find the std bmi of males
m_sd #std bmi for males is 6.135802254619795

m_med = np.median(a['bmi'][male]) #Find the median bmi for males
m_med #median bmi for males is 30.7

##FEMALES
f_mn = a['bmi'][~male].mean() #Find the mean bmi of females
f_mn #mean bmi of females is 30.3797583081571

f_sd = a['bmi'][~male].std() #Find the std bmi of females
f_sd #std bmi of females is 6.041939120876393

f_med = np.median(a['bmi'][~male]) #Find the median bmi for females
f_med #median bmi of females is 30.1

#Male/female BMI means
print('Male mean: {:.2f} \nFemale mean: {:.2f}'.format(m_mn, f_mn)) 

#Male/female BMI stds
print('Male std: {:.2f} \nFemale std: {:.2f}'.format(m_sd, f_sd)) 

#Male/female BMI median
print('Male median: {:.2f} \nFemale median: {:.2f}'.format(m_med, f_med)) 

#find mean, sd, and median of bmi grouped by smoking/nonsmoking
##Smokers

smoke = a['smoker'] == b'yes'
smoke_mn = a['bmi'][smoke].mean() #find mean bmi

smoke_sd = a['bmi'][smoke].std() #find std bmi

smoke_med = np.median(a['bmi'][smoke]) #find median bmi

##Nonsmokers

nsmoke_mn = a['bmi'][~smoke].mean() #find mean bmi

nsmoke_sd = a['bmi'][~smoke].std() #find std bmi

nsmoke_med = np.median(a['bmi'][~smoke]) #find median bmi

#Smoker/Nonsmoker BMI means
print('Smoker mean: {:.2f} \nNonsmoker mean: {:.2f}'.format(smoke_mn, nsmoke_mn)) 

#Smoker/Nonsmoker BMI stds
print('Smoker std: {:.2f} \nNonsmoker std: {:.2f}'.format(smoke_sd, nsmoke_sd)) 

#Smoker/Nonsmoker BMI median
print('Smoker median: {:.2f} \nNonsmoker median: {:.2f}'.format(smoke_med, nsmoke_med))

#find mean, sd, and median of bmi grouped by region
##Northeast

ne = a['region'] == b'northeast'

ne_mn = a['bmi'][ne].mean() #find mean bmi

ne_sd = a['bmi'][ne].std() #find std bmi

ne_med = np.median(a['bmi'][ne]) #find median bmi

##Northwest
nw = a['region'] == b'northwest'

nw_mn = a['bmi'][nw].mean() #find mean bmi

nw_sd = a['bmi'][nw].std() #find std bmi

nw_med = np.median(a['bmi'][nw]) #find median bmi

##Southeast

se = a['region'] == b'southeast'

se_mn = a['bmi'][se].mean() #find mean bmi

se_sd = a['bmi'][se].std() #find std bmi

se_med = np.median(a['bmi'][se]) #find median bmi

##Southwest

sw = a['region'] == b'southwest'

sw_mn = a['bmi'][sw].mean() #find mean bmi

sw_sd = a['bmi'][sw].std() #find std bmi

sw_med = np.median(a['bmi'][sw]) #find median bmi

#Region BMI means
print('Northeast mean: {:.2f} \nNorthwest mean: {:.2f} \nSoutheast mean: {:.2f} \nSouthwest mean: {:.2f}'\
      .format(ne_mn, nw_mn, se_mn, sw_mn)) 

#Region BMI std
print('Northeast std: {:.2f} \nNorthwest std: {:.2f} \nSoutheast std: {:.2f} \nSouthwest std: {:.2f}'\
      .format(ne_sd, nw_sd, se_sd, sw_sd)) 

#Region BMI median
print('Northeast median: {:.2f} \nNorthwest median: {:.2f} \nSoutheast median: {:.2f} \nSouthwest median: {:.2f}'\
      .format(ne_med, nw_med, se_med, sw_med)) 

#find mean, sd, and median bmi of people with > 2 children

child = a['children'] > 2 #find people who have more than 2 children

child_mn = a['bmi'][child].mean() #find mean bmi

child_sd = a['bmi'][child].std() #find std bmi

child_med = np.median(a['bmi'][child]) #find median bmi
##print the mean, std, and median bmi of people with more than 2 children
print('BMI mean of people with more than 2 children: {:.2f}\
      \nBMI std of people with more than 2 children: {:.2f}\
      \nBMI median of people with more than 2 children: {:.2f}'\
      .format(child_mn, child_sd, child_med))


##less than 2 children

ch_mn = a['bmi'][~child].mean() #find mean bmi

ch_sd = a['bmi'][~child].std() #find std bmi

ch_med = np.median(a['bmi'][~child]) #find median bmi
##print the mean, std, and median bmi of people with more than 2 children
print('BMI mean of people with less than 2 children: {:.2f}\
      \nBMI std of people with less than 2 children: {:.2f}\
      \nBMI median of people with less than 2 children: {:.2f}'\
      .format(ch_mn, ch_sd, ch_med))

##How do the factors affect BMI###

#####Smoking Habit:

#The median BMI for smokers is 30.45 while the 
#median BMI for nonsmokers is 30.35. Since the median is approximately 
#the same for both smokers and nonsmokers, the mean and standard deviations
#will be able to determine whether smoking has an effect on BMI. 
#The mean BMI for smokers is 30.71 with a standard deviation of 6.31 making the range
#approximately (24.4, 37.02). The mean BMI for nonsmokers is 30.65 with a standard deviation
#of 6.04 making the range approximately (24.61,36.69). Since both smoking and nonsmoking BMI's fall within
#the same range, smoking does not affect BMI. 


####Region:

#Northeast:

#The median BMI is 28.90. The mean is 29.18 with a standard deviation of 5.93. The range is approximately 
#(23.25, 35.11)

#Northwest:

#The median BMI is 28.90. The mean is 29.20 with a standard deviation of 5.13. The range is approximately 
#(24.07, 34.33)

#Southeast:

#The median BMI is 33.30. The mean is 33.36 with a standard deviation of 6.47. The range is approximately 
#(26.89, 39.83)

#Southwest:

#The median BMI is 30.30. The mean is 30.60 with a standard deviation of 5.68. The range is approximately 
#(24.92, 36.28)

###Based off of these ranges, there is enough evidence to assume that region has 
#an effect on BMI, specifically, living in the South region (mainly Southeast)
#may contribute to a higher BMI. 

####Children:

#The median BMI for people with more than two children is 30.35 while the median BMI
#for people with less than two children is 30.40. The mean BMI for people with more
#than two children is 30.68 with a standard deviation of 5.76, making the range approximately 
#(24.92, 36.44). The mean BMI for people with less than two children is 
#30.66 with a standard deviation of 6.15, making the range approximately 
#(24.51,36.81). Since these two means seem to be within the same range within one standard deviation,
#it can be inferenced that the amount of children a person has is not a contributing factor to BMI. 

##Sort data by expense

exp = np.sort(a, order='expenses') #sort data by expenses 
exp[:] = exp[::-1] #sort data in decreasing order by expenses
exp
top_twen = exp[:267,] #top 20%
top_twen


toptwen1 = exp[:len(exp)//267].copy()
#Compute mean, std, and mode of bmi of smoker/nonsmoker

##Smokers

top_smoke = top_twen['smoker'] == b'yes'
tsm_mn = top_twen['bmi'][top_smoke].mean() #find mean bmi
tsm_mn #avg bmi 32.646153846153844

tsm_sd = top_twen['bmi'][top_smoke].std() #find std bmi
tsm_sd #5.74663652591207

from scipy import stats

tsm_mode = stats.mode(top_twen['bmi'][top_smoke])
tsm_mode #mode BMI is 30.8
t_mode = 30.8
##Nonsmokers

tnonsm_mn = top_twen['bmi'][~top_smoke].mean() #find mean bmi
tnonsm_mn #avg bmi 30.788135593220336

tnonsm_sd = top_twen['bmi'][~top_smoke].std() #find std bmi
tnonsm_sd #5.410005944599093

tnonsm_mode = stats.mode(top_twen['bmi'][~top_smoke])
tnonsm_mode #mode BMI is 27.6
tn_mode = 27.6

#Smoker/Nonsmoker BMI means
print('Smoker mean: {:.2f} \nNonsmoker mean: {:.2f}\
      \nSmoker std: {:.2f} \nNonsmoker std: {:.2f}\
      \nSmoker mode:  \nNonsmoker mode: {:.1f}'\
      .format(tsm_mn, tnonsm_mn, tsm_sd, tnonsm_sd, t_mode, tn_mode)) 

#Compute mean, std, and mode of bmi by region

##Northeast

netop = top_twen['region'] == b'northeast'

netop_mn = top_twen['bmi'][netop].mean() #find mean bmi
netop_mn #mean BMI is 30.906060606060606

netop_sd = top_twen['bmi'][netop].std() #find std bmi
netop_sd #std BMI is 5.083660062660616

netop_mode = stats.mode(top_twen['bmi'][netop]) #find mode bmi
netop_mode #mode BMI is 24.3
net_mode = 24.3

##Northwest
nwtop = top_twen['region'] == b'northwest'

nwtop_mn = top_twen['bmi'][nwtop].mean() #find mean bmi
nwtop_mn #mean BMI is 30.167796610169493

nwtop_sd = top_twen['bmi'][nwtop].std() #find std bmi
nwtop_sd #std BMI is 5.2122554627991935

nwtop_mode = stats.mode(top_twen['bmi'][nwtop]) #find mode bmi
nwtop_mode #mode BMI is 23.7
nwt_mode = 23.7

##Southeast

setop = top_twen['region'] == b'southeast'

setop_mn = top_twen['bmi'][setop].mean() #find mean bmi
setop_mn #mean BMI is 34.28977272727273

setop_sd = top_twen['bmi'][setop].std() #find std bmi
setop_sd #std BMI is 6.4848081168206875

setop_mode = stats.mode(top_twen['bmi'][setop]) #find mode bmi
setop_mode #mode BMI is 38.1
set_mode = 38.1

##Southwest

swtop = top_twen['region'] == b'southwest'

swtop_mn = top_twen['bmi'][swtop].mean() #find mean bmi
swtop_mn #mean BMI is 32.772222222222226

swtop_sd = top_twen['bmi'][swtop].std() #find std bmi
swtop_sd #std BMI is 4.280507786884664

swtop_mode = stats.mode(top_twen['bmi'][swtop]) #find mode bmi
swtop_mode #mode BMI is 34.8
swt_mode = 34.8

#Region BMI means, stds, and modes 
print('Northeast: \n mean: {:.2f} \n std: {:.2f} \n mode: {:.2f} \
      \nNorthwest: \n mean: {:.2f} \n std: {:.2f} \n mode: {:.2f} \
      \nSoutheast: \n mean: {:.2f} \n std: {:.2f} \n mode: {:.2f} \
      \nSouthwest: \n mean: {:.2f} \n std: {:.2f} \n mode: {:.2f}'\
      .format(netop_mn, netop_sd, net_mode, nwtop_mn, nwtop_sd, nwt_mode,\
              setop_mn, setop_sd, set_mode, swtop_mn, swtop_sd, swt_mode))


#Find mean, std, and mode of the rest of the 80% of population
eight_perc = exp[268:,] #rest of 80%
eight_perc

#Compute mean, std, and mode of bmi of smoker/nonsmoker

##Smokers

low_smoke = eight_perc['smoker'] == b'yes'
lowsm_mn = eight_perc['bmi'][low_smoke].mean() #find mean bmi
lowsm_mn #avg bmi 24.62121212121212


lowsm_sd = eight_perc['bmi'][low_smoke].std() #find std bmi
lowsm_sd #3.5068122082734203


lowsm_mode = stats.mode(eight_perc['bmi'][low_smoke])
lowsm_mode #mode BMI is 28.3
low_mode = 28.3


##Nonsmokers

lnonsm_mn = eight_perc['bmi'][~low_smoke].mean() #find mean bmi
lnonsm_mn #avg bmi 330.64631474103586

lnonsm_sd = eight_perc['bmi'][~low_smoke].std() #find std bmi
lnonsm_sd #6.077715185580326

lnonsm_mode = stats.mode(eight_perc['bmi'][~low_smoke])
lnonsm_mode #mode BMI is 28.9
lown_mode = 28.9

#Smoker/Nonsmoker BMI means
print('Smoker mean: {:.2f} \nNonsmoker mean: {:.2f}\
      \nSmoker std: {:.2f} \nNonsmoker std: {:.2f}\
      \nSmoker mode:  \nNonsmoker mode: {:.1f}'\
      .format(lowsm_mn, lnonsm_mn, lowsm_sd, lnonsm_sd, low_mode, lown_mode)) 

#Compute mean, std, and mode of bmi by region

##Northeast

nelow = eight_perc['region'] == b'northeast'

nelow_mn = eight_perc['bmi'][nelow].mean() #find mean bmi
nelow_mn #mean BMI is 28.730350194552532

nelow_sd = eight_perc['bmi'][nelow].std() #find std bmi
nelow_sd #std BMI is 6.057462602836007

nelow_mode = stats.mode(eight_perc['bmi'][nelow]) #find mode bmi
nelow_mode #mode BMI is 25.5
nel_mode = 25.5

##Northwest
nwlow = eight_perc['region'] == b'northwest'

nwlow_mn = eight_perc['bmi'][nwlow].mean() #find mean bmi
nwlow_mn #mean BMI is 28.987593984962405

nwlow_sd = eight_perc['bmi'][nwlow].std() #find std bmi
nwlow_sd #std BMI is 5.08460342164977

nwlow_mode = stats.mode(eight_perc['bmi'][nwlow]) #find mode bmi
nwlow_mode #mode BMI is 27.6
nwl_mode = 27.6

##Southeast

selow = eight_perc['region'] == b'southeast'

selow_mn = eight_perc['bmi'][selow].mean() #find mean bmi
selow_mn #mean BMI is 33.062681159420286

selow_sd = eight_perc['bmi'][selow].std() #find std bmi
selow_sd #std BMI is  6.437037760509468

selow_mode = stats.mode(eight_perc['bmi'][selow]) #find mode bmi
selow_mode #mode BMI is 38.1
sel_mode = 29.9

##Southwest

swlow = eight_perc['region'] == b'southwest'

swlow_mn = eight_perc['bmi'][swlow].mean() #find mean bmi
swlow_mn #mean BMI is 30.163099630996314

swlow_sd = eight_perc['bmi'][swlow].std() #find std bmi
swlow_sd #std BMI is 5.826732831058809

swlow_mode = stats.mode(eight_perc['bmi'][swlow]) #find mode bmi
swlow_mode #mode BMI is25.8
swl_mode = 25.8

#Region BMI means, stds, and modes for 80%
print('Northeast: \n mean: {:.2f} \n std: {:.2f} \n mode: {:.2f} \
      \nNorthwest: \n mean: {:.2f} \n std: {:.2f} \n mode: {:.2f} \
      \nSoutheast: \n mean: {:.2f} \n std: {:.2f} \n mode: {:.2f} \
      \nSouthwest: \n mean: {:.2f} \n std: {:.2f} \n mode: {:.2f}'\
      .format(nelow_mn, nelow_sd, nel_mode, nwlow_mn, nwlow_sd, nwl_mode,\
              selow_mn, selow_sd, sel_mode, swlow_mn, swlow_sd, swl_mode))

######COMPARISON BETWEEN TOP 20% AND BOTTOM 80%
#Based off of the data of the smoking/nonsmoking population, the top 20% of 
#the population seems to have a higher average BMI compared to the lower
#80% of the population in both smokers and nonsmokers.

#Based off of the data by region, the top 20% of the population had a 
#lower average BMI across all regions compared to the lower 80% of the 
#population. This means that with respect to region, the lower 80% of 
#the population has a higher BMI compared to the top 20% of the population 
#across all regions. 

#Save the adjusted arrays into new text files 
np.savetxt('adjusted insurance file.txt', a, delimiter=" ", fmt="%s") #adjusted array with all data
np.savetxt('expense sorted.txt', exp, delimiter=" ", fmt="%s") #data sorted by expenses