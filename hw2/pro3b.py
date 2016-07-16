def nbitIntToDigits(i,n):
	bin_num=bin(i)
	bin_num=str(bin_num)
	bin_num=bin_num[2:len(bin_num)]
	bin_num= list(bin_num)

	if len(bin_num)<n:
		head=(n-len(bin_num))*['0']
		head.extend(bin_num)
		return head

	else:
		return bin_num[0:n]




def main():
	output_list=[nbitIntToDigits(3,2),nbitIntToDigits(3,6),nbitIntToDigits(11,4)]
	print(output_list)

main()
