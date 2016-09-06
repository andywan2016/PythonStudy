import collections
import re
import urllib.request
import sys

#modulename='urllib'
#print(modulename in sys.modules)




url='https://courseworks.columbia.edu/access/content/group/COMSW3101_002_2015_3/week3/hamlet.html'

with urllib.request.urlopen(url) as ef:
    for bin in ef:
        print(bin)
        s=bin.decode('utf-8')
        print(s)
        break