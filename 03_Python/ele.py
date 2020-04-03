# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 09:03:26 2020

"""
import csv

file = open("Resources/election_data.csv")

csv_reader = csv.reader(file)

eldict ={}
elist = []
header = next(csv_reader)
tvotes = 0
winner = ""
wvotes = 0 

for  i in csv_reader:
    tvotes = tvotes + 1
    if i[2] not in elist:
        elist.append(i[2])
        eldict[i[2]] = 1
    eldict[i[2]] = eldict[i[2]] + 1
    
for i in eldict:
    cvotes = eldict.get(i)
    cper = round((cvotes/tvotes)*100)
    if cvotes > wvotes:
        winner = i
        wvotes = cvotes
    print(i,cper,cvotes)
print(winner)


