import collections
import re
import urllib.request
import sys
import string   

#modulename='urllib'
#print(modulename in sys.modules)

url='https://courseworks.columbia.edu/access/content/group/COMSW3101_002_2015_3/week3/hamlet.html'

line_num=0
tmp_str=" "
with urllib.request.urlopen(url) as ef:
    for bin in ef:
        line_num+=1
        #print(bin)
        s=bin.decode('utf-8')
        tmp_str=s
        #print(s)
        if line_num==1:
            break
        
###below are test for regular expression and learning
splited=tmp_str.split()
re_result=re.findall("/[A-Z]+/",splited[1])


#print(line_num)
print(tmp_str)
print(splited)
print(re_result)