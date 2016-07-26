def countBases(dna):
	board=[0,0,0,0]
	for x in dna:
		if x=='A':
			board[0]+=1
		elif x=='C':
			board[1]+=1
		elif x=='G':
			board[2]+=1
		elif x=='T':
			board[3]+=1
		else:
			print("invalid dna kye")
			return None

	return board


def main():
	bases='ACGT'
	dna='CATCGATATCTCTGAGTGCAC'
	print(countBases('AC'))
	print(countBases(dna))


main()
