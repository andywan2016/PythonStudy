import string
from pro1 import swapaz,bad,bad2

def ifSame(strr):
	for x in range(len(strr)-1):
		if strr[x] in strr[x+1:]:
			return False
	return True



def goodperm(cl):
	al=string.ascii_lowercase
	al_new=cl.encode(al)
	if len(al_new)!=26:
		return False
	#al_new1=""        
	#for e in al:
	#	coded=cl.encode(e)
	#	if e!=coded:
		#	al_new1+=coded
	return ifSame(al_new)

	




def main():
	result=[goodperm(c) for c in [swapaz(), bad(), bad2()]]
	print(result)


main()
