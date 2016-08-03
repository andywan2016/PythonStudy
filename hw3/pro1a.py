import string
from pro1 import swapaz,bad,bad2


def goodperm(cl):
	al=string.ascii_lowercase
	al_new=cl.encode(al)
	if len(al_new)!=26:
		return False
	al_new1=""        
	for e in al:
		coded=cl.encode(e)
		if e!=coded:
			al_new1+=coded
	




def main():
	[goodperm(c) for c in [swapaz(), bad(), bad2()]]

	return(None)


main()
