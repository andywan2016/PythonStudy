def powerSet(l):
	output_list=[]
	output_list.append([])
	
	for e in l:
		for x in output_list:
			tmp=x
			tmp.append(e)
			output_list.append(tmp)


def main():
	ls=powerSet(['avery','math','butler'])
	print(ls)

main()
