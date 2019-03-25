"""
Created on Mon Mar 25 21:42:17 2019

@author: Sakib
"""
f = open("train.txt", "r")
o = open("train_formatted.csv", "a")


for item in range (2):
    first=f.readline()
    second=f.readline()
    third=f.readline()
    out=second.rstrip()+","+third
    print(out)
    o.write(out)

f.close()
o.close()
