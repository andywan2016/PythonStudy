"""

def powerSet(l):
	output_list=[]
	output_list.append([])
	
	for e in l:
		for x in output_list:
			tmp=x
			tmp.append(e)
			output_list.append(tmp)
"""
#this function is used for
def listExtend(ls,element):
	ls1,ls2=[],[]
	ls1.extend(ls)
	ls2.extend(ls)
	#ls1.extend(" ")
	ls2.append(element)
	return [ls1,ls2]


def powerSet(l):
	output=[[]]
	for x in l:
		tmpList=[]
		for y in output:
			tmpList.extend(listExtend(y,x))
		output=[]
		output.extend(tmpList)

	return output


def main():
#test for listExtend	
#	print(listExtend(["A1","B1","C1"],"D1"))
	
	ls=powerSet(['avery','math','butler'])
	print(ls)

main()
