# the test part is in 5a just for convinience

def reverseComplement(dna):
	strr=""
	for i in range(len(dna)):
		if dna[i]=='A':
			strr+='T'
			#dna[i]='T'
		elif dna[i]=='T':
			strr+='A'
			#dna[i]='A'
		elif dna[i]=='C':
			strr+='G'
			#dna[i]='G'
		elif dna[i]=='G':
			strr+='C'
			#dna[i]='C'
		else:
			print("invald DNA element")
			return None
	return strr
