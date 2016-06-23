# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 00:39:12 2016

@author: Andy
"""
#problem 2:
def rle(l):
    if len(l)==0:
        return []
    else:
        output=[[l[0],1]]
        i=1
        while i<len(l):
            if output[-1][0]==l[i]:
                output[-1][1]+=1
            else:
                output.append([l[i],1])
            i+=1           
        return output 
        
print(rle([]))
print(rle([5]))
print(rle([2,2]))
print(rle([1,2]))
print(rle([10,10,20,33,33,33,33,10,1,30,30,7]))