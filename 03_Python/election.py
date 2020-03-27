# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:28:50 2020

@author: 517889
"""

import os
import csv

Poll = os.path.join("Resources/election_data.csv")

with open(Poll, encoding="utf-8") as csvfile:
    
    poll_reader = csv.reader(csvfile, delimiter=",")
    
    header = next(poll_reader)
    
    poll_dict = {"Khan": 0, "Correy":0, "Li":0, "O'Tooley":0} #dict
    totalvotes = 0;
    for row in poll_reader:
        totalvotes +=1
        poll_dict[row[2]] = poll_dict[row[2]] + 1
           
kvotes = (poll_dict['Khan'])
kper = round(((poll_dict['Khan'])/totalvotes)*100 ,2)

cvotes = (poll_dict['Correy'])
cper = round(((poll_dict['Correy'])/totalvotes)*100 ,2)
    
lvotes = (poll_dict['Li'])
lper = round(((poll_dict['Li'])/totalvotes)*100 ,2)

name = "O'Tooley"
ovotes = (poll_dict[name])
oper = round(((poll_dict[name])/totalvotes)*100 ,2)



title = "Election Results\n"    
L1 ="----------------------------\n"
L2 = "Total Votes: "
L3 ="----------------------------\n"
L4 = "Khan: "
L5 = "Correy: "
L6 = "Li: "
L7 = "O'Tooley: "
L8 = "Winner: Khan"

print(title,L1)
print(L2, totalvotes)
print(L3)  
print(L4, kper, "% (", kvotes, ")")      
print(L5, cper, "% (", cvotes, ")")      
print(L6, lper, "% (", lvotes, ")")   
print(L7, oper, "% (", ovotes, ")")   
print(L3)  
print(L8) 
print(L3) 

file = open("election_result.txt",'w')
file.write(title)
file.write(L1)
file.write(L2 + str(totalvotes) + '\n')
file.write(L3)
file.write(L4 + str(kper) + "% (" + str(kvotes) + ")" +'\n')
file.write(L5 +  str(cper) + "% (" + str(cvotes) +  ")" +'\n')
file.write(L6 + str(lper) + "% (" + str(lvotes) +  ")" + '\n')
file.write(L7 + str(oper) + "% (" + str(ovotes) +  ")" + '\n')
file.write(L3)
file.write(L8 + '\n')
file.write(L3)
file.close()



  
















