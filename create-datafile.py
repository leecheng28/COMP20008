# This Python file uses the following encoding: utf-8

# Data Pre-processing and Integration
# Author: Li Cheng. ID: 688819.

import csv

# Procedures for data pre-processing---
# Read data, from the business-count.csv file, in column C(CULE small area) and column X(Total establishments in block), to store the number of business establishments in each suburb into a dictionary.
# There are no duplicates of suburb in the dictionary N. ie. each suburb occurs once
# An example:  dict_N={“CBD”: 1, “Carlton”:2, "Brunswick":5555, …}

# categorise data baesd on each suburb. In the form: N={“CBD”: 1, “Carlton”:2, "Brunswick":5555, …}
dict_N={}
list_suburb_N=[]
list_count_N=[]# extract useful data from file

with open('business-count.csv') as csvfile:
    reader = csv.DictReader(csvfile)
# get the list of values in list form. eg.['', '', '', ...]
    for column in reader:
        list_suburb_N.append(column['CLUE_small_area'])
        list_count.append(column['Total_establishments_in_block'])

idx_N=0 # index of current suburb in the list of suburb
for suburb in list_suburb_N:
    if suburb not in dict_N:
        dict_N[suburb]=int(list_count[idx_N])
    else: # suburb already exists in the dictionary
        dict_N[suburb]+=int(list_count[idx_N])
    idx_N+=1
print dict_N

# now do the same step of categorising date for unemploy-rate.csv file
# An example of required dictionary: dict_UR={UR= {“CBD”: 0.05, “Carlton”: 0.025, 'Brunswick': 0.01, …}}
'''
dict_UR={}
list_suburb_UR=[]
list_average_UR=[]
with open('employ-rate.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for column in reader:
        list_suburb_UR.append(column['Statistical Area Level 2 (SA2)'])
        list_average_UR.append(column['Average'])
idx_UR=0 # index of current suburb in the list of suburb
for suburb in list_suburb_UR:
    if suburb not in dict_UR:
        dict_UR[suburb]=int(list_average_UR[idx_UR])
    else: # suburb already exists in the dictionary
        dict_UR[suburb]+=int(list_average_UR[idx_UR])
    idx_UR+=1
print dict_UR
'''
# Prodecures for data integration---