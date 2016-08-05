import pickle
from pro1 import swapaz,bad,bad2

keypath = "./tmp/key.pickle"

pickle.dump(swapaz(),open(keypath,'wb'))
