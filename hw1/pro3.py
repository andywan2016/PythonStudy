# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 01:26:35 2016

@author: Andy
"""

def partition(l,n,overlap):
    if type(l) is range:
        return 0
    if type(l) is list:
        return 1
    else:
        print("unsupported type")
        return None
        
def main():
    print(partition(range(10),0,1))
    print(partition(list(range(10)),0,1))
    print(partition(1,0,1))

main()