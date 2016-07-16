def select(l,selectors):
	if len(l)!=len(selectors):
		print("length of two list must be same")
		return None
	
	else:
		output_list=[]
		for i in range(len(list(l))):
			if bool(list(selectors)[i]) is True:
				output_list+=[list(l)[i]]
		return output_list




def main():
	ls=select(range(5),[0,1,'',"foo",True])
	print(ls)

main()
