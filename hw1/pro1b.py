from pro7 import dp

def shortlong(tv0,tv1):
  if len(tv0)<len(tv1):
    l=[tv0,len(tv0),tv1,len(tv1)]
  else:
    l=[tv1,len(tv1),tv0,len(tv0)]
  return l

#problem 1c
def odp(tv0,tv1,offset):
	info=shortlong(tv0,tv1)
	if offset>(info[3]-info[1]):
		print("offset number too large")
		return None
	else:
		return dp(info[0],info[2][offset:])


#problem 1d
def dpd(tv0,tv1,pad):
  global s,l
  s,sl,l,ll=shortlong(tv0,tv1)
  #print type(s)
 # print s
 # print hex(id(s))
  dl=ll-sl
  s=s[:]
 # print s
 # print hex(id(s))
  #print type(s) 
  s.extend(dl*[pad])
 
  #print hex(id(s))
  return dp(s,l)




def main():
  a=[1,2,3]
  b=[4,5,6,7,8,9]
  #print shortlong(a,b)
 # c1=[odp(a,b,0),odp(a,b,1),odp(a,b,2)]
  #print c1  
 # d1=[dpd(a,b,0),dpd(a,b,1),dpd(a,b,2)]
 # print d1
 # print(dpd(a,b,1))
  print(dpd(a,b,2))  


main()
