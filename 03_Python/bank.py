# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
import os
import csv

csv_path = os.path.join("Resources","budget_data.csv")
month = []
pl = []
totalmonth = 0

with open (csv_path) as budgetdata:
    csv_reader = csv.reader(budgetdata,delimiter = ",")
    csv_header = next(csv_reader)
    
#    print(csv_header)
    
    for rows in csv_reader:
        
        month.append(rows[0])
        pl.append(int(rows[1]))
        
totalmonth = len(month)
totalpl= 0
for i in range(0, len(pl)):
    totalpl = int(pl[i]) + totalpl    
    average = round(totalpl / totalmonth)
    inc = max(pl)
    a = (pl.index(inc))
    incmon = month[a]
    dec = min(pl)
    b = (pl.index(dec))
    decmon = month[b]
    
title = "Financianl Analysis\n"    
L1 ="----------------------------\n"
L2 = "Total Months: "
L3 = "Total: $" 
L4 = "Average Change: $"
L5 = "Greatest Increase in Profits: "
L6 = "Greatest Decrease in Profits: "

print(title,L1)
print(L2, totalmonth)
print(L3, totalpl)  
print(L4,  average)      
print(L5, incmon ,"($", inc, ")")      
print(L6,decmon, "($",dec, ")")     

file = open("budget_result.txt",'w')
file.write(title)
file.write(L1)
file.write(L2 + str(totalmonth) + '\n')
file.write(L3 + str(totalpl) + '\n')
file.write(L4 + str(average) + '\n')
file.write(L5 +  str(incmon) + '($' + str(inc) + ')\n')
file.write(L6 + str(decmon) + '($'+ str(dec) + ')\n')
file.close()