import collections
import re
import urllib.request
import sys
import string   


from bs4 import BeautifulSoup

#modulename='urllib'
#print(modulename in sys.modules)

url='https://courseworks.columbia.edu/access/content/group/COMSW3101_002_2015_3/week3/hamlet.html'


#initial line and word count
line_num=0
word_num=0
#this is used for check the current line 
tmp_str=" "

def CheckContent(s):
    return (not (re.match('<A NAME=.+>.+</A><br>',s) is None))


def Checkb(s):
	return re.match('<b>.+</b>',s)


with urllib.request.urlopen(url) as ef:
   # soup=BeautifulSoup(ef, 'html.parser')
   # print(soup.b.attrs)

   # print(soup.prettify())

    for bin in ef:
        line_num+=1
        #print(bin)
        s=bin.decode('utf-8')
        tmp_str=s
        if not CheckContent(s):
            currentLine_wordCount=len(re.findall('speech',tmp_str))
        #currentLine_wordCount=len(re.findall('[A-z]+',tmp_str))
            word_num+=currentLine_wordCount
	if not(Checkb(s) is None):
#######################################################		
	  	
       # print(s)
       # if line_num==100:
         #   break

    



        
###below are test for regular expression and learning
#splited=tmp_str.split()
#re_result=re.findall('[A-z]+',tmp_str)


print(line_num)
print(word_num)
#print(tmp_str)
#print(CheckContent(tmp_str))
#print(splited)
#print(re_result)




