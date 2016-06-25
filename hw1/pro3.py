# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 01:26:35 2016

@author: Andy
"""

def partition(l,n,overlap):
    ls=list(l)
    ls.append(ls[-1]+1)
    if len(ls)<n:
        return None
    else:
        output=[range(ls[0],ls[n])]
        i=n-overlap
        while i+n <len(ls):
            output.append(range(ls[i],ls[i+n]))
            i+=n-overlap
        if type(l) is range:
            return output
        if type(l) is list:
            return list(map(list,output))
        else:
            print("unsupported type")
            return None

        
def main():
    print(partition(range(10),2,1))
    print(partition(list(range(10)),2,0))
   # print(partition(1,0,1))

main()
