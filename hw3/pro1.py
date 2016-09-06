import string

#alphabet=string.ascii_lowercase

#print(alphabet)

class swapaz:
	def encode(self,s):
		s=s.replace('a','A').replace('z','Z').replace('Z','a').replace('A','z')
		return(s)


	def decode(self,s):
		return(self.encode(s))

#s=swapaz()
#e=s.encode('larry')
#print(e)

#s.decode(e)

class bad:
	def encode(self,s):
		return('x')

	def decode(self,s):
		return('xy')


class bad2:
	def encode(self,s):
		return(''.join(['b' if e=='a' else e for e in s]))
	
	def decode(self,s):
		return(s)



		


















