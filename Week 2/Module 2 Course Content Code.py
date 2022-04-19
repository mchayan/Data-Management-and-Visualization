# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:50:43 2015

@author: ldierker
"""
import pandas
import numpy
# any additional libraries would be imported here

data = pandas.read_csv('nesarc_pds.csv', low_memory=False)

print (len(data)) #number of observations (rows)
print (len(data.columns)) # number of variables (columns)


# checking the format of your variables
data['ETHRACE2A'].dtype

#setting variables you will be working with to numeric 
data['TAB12MDX'] = pandas.to_numeric(data['TAB12MDX'])
data['CHECK321'] = pandas.to_numeric(data['CHECK321'])
data['S3AQ3B1'] = pandas.to_numeric(data['S3AQ3B1'])
data['S3AQ3C1'] = pandas.to_numeric(data['S3AQ3C1'])
data['AGE'] = pandas.to_numeric(data['AGE'])

#counts and percentages (i.e. frequency distributions) for each variable
c1 = data['TAB12MDX'].value_counts(sort=False)
print (c1)

p1 = data['TAB12MDX'].value_counts(sort=False, normalize=True)
print (p1)

c2 = data['CHECK321'].value_counts(sort=False)
print(c2)

p2 = data['CHECK321'].value_counts(sort=False, normalize=True)
print (p2)

c3 = data['S3AQ3B1'].value_counts(sort=False)
print(c3)

p3 = data['S3AQ3B1'].value_counts(sort=False, normalize=True)
print (p3)

c4 = data['S3AQ3C1'].value_counts(sort=False)
print(c4)

p4 = data['S3AQ3C1'].value_counts(sort=False, normalize=True)
print (p4)

c4 = data['S3AQ3C1'].value_counts(sort=False)
print(c4)

p4 = data['S3AQ3C1'].value_counts(sort=False, normalize=True)
print (p4)

#ADDING TITLES
print ('counts for TAB12MDX')
c1 = data['TAB12MDX'].value_counts(sort=False)
print (c1)
#print (len(data['TAB12MDX'])) #number of observations (rows)

print ('percentages for TAB12MDX')
p1 = data['TAB12MDX'].value_counts(sort=False, normalize=True)
print (p1)

print ('counts for CHECK321')
c2 = data['CHECK321'].value_counts(sort=False)
print(c2)

print ('percentages for CHECK321')
p2 = data['CHECK321'].value_counts(sort=False, normalize=True)
print (p2)

print ('counts for S3AQ3B1')
c3 = data['S3AQ3B1'].value_counts(sort=False, dropna=False)
print(c3)

print ('percentages for S3AQ3B1')
p3 = data['S3AQ3B1'].value_counts(sort=False, normalize=True)
print (p3)

print ('counts for S3AQ3C1')
c4 = data['S3AQ3C1'].value_counts(sort=False, dropna=False)
print(c4)

print ('percentages for S3AQ3C1')
p4 = data['S3AQ3C1'].value_counts(sort=False, dropna=False, normalize=True)
print (p4)

#ADDING MORE DESCRIPTIVE TITLES
print('counts for TAB12MDX – nicotine dependence in the past 12 months')
c1 = data['TAB12MDX'].value_counts(sort=False)
print (c1)

print('percentages for TAB12MDX nicotine dependence in the past 12 months')
p1 = data['TAB12MDX'].value_counts(sort=False, normalize=True)
print (p1)

print('counts for CHECK321 smoked in the past year')
c2 = data['CHECK321'].value_counts(sort=False)
print(c2)

print('percentages for CHECK321 smoked in the past year')
p2 = data['CHECK321'].value_counts(sort=False, normalize=True)
print (p2)

print('counts for S3AQ3B1 –usual frequency when smoked cigarettes')
c3 = data['S3AQ3B1'].value_counts(sort=False)
print(c3)

print('percentages for S3AQ3B1 - usual frequency when smoked cigarettes')
p3 = data['S3AQ3B1'].value_counts(sort=False, normalize=True)
print (p3)

print('counts for S3AQ3C1 usual quantity when smoked cigarettes')
c4 = data['S3AQ3C1'].value_counts(sort=False, dropna=False)
print(c4)

print('percentages for S3AQ3C1 usual quantity when smoked cigarettes')
p4 = data['S3AQ3C1'].value_counts(sort=False, normalize=True)
print (p4)

# frequency distributions using the 'bygroup' function
ct1= data.groupby('TAB12MDX').size()
print(ct1)

pt1 = data.groupby('TAB12MDX').size() * 100 / len(data)
print(pt1)

#subset data to young adults age 18 to 25 who have smoked in the past 12 months
sub1=data[(data['AGE']>=18) & (data['AGE']<=25) & (data['CHECK321']==1)]

#make a copy of my new subsetted data
sub2 = sub1.copy()

# frequency distributions on new sub2 data frame
print('counts for AGE')
c5 = sub2['AGE'].value_counts(sort=False)
print(c5)

print('percentages for AGE')
p5 = sub2['AGE'].value_counts(sort=False, normalize=True)
print (p5)

print('counts for CHECK321')
c6 = sub2['S2AQ8A'].value_counts(sort=False)
print(c6)

print('percentages for CHECK321')
p6 = sub2['CHECK321'].value_counts(sort=False, normalize=True)
print (p6)

#upper-case all DataFrame column names - place afer code for loading data aboave
data.columns = list(map(str.upper, data.columns))

# bug fix for display formats to avoid run time errors - put after code for loading data above
pandas.set_option('display.float_format', lambda x:'%f'%x)


