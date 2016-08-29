import pickle
from pro1 import swapaz,bad,bad2

#keypath = "./tmp/key.pickle"





#pickle.dump(swapaz(),open(keypath,'wb'))



def saveKey(path,key):
	if key==None:
		raise Exception("bad key")
	else:
		pickle.dump(key,open(path,'wb'))




#key1=None

#saveKey(keypath,key1)

