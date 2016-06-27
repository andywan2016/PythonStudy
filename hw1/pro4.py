#for part a
def expandlazy(l):
	if type(l) in  [zip,range,enumerate]:
		return list(l)
	else:
		return l
#for part b
def expandlazylist(l):
	return list(map(expandlazy,l))





def main():
	lla=[expandlazy(234),expandlazy(range(3)),expandlazy('asdf'),expandlazy(enumerate(['a','b','c',]))]
	print(lla)
	llb=[1,2,3,range(4),5,zip([1,2,3],[4,5]),'asdf',enumerate(['a','b','c'])]

	print(expandlazylist(llb))



#	expandlazy(123)




main()
