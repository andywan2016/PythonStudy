from pro1b import saveKey

def encode_in(string):
    output=string.replace('a','A').replace('z','Z').replace('Z','a').replace('A','z')
    return(output)


def decode_in(string):
    return(encode(string))


def encode(path,string):
    coded_str=encode_in(string)
    saveKey(path,coded_str)
    return(coded_str)


def decode(path,string):
    #coded_str=pickle.load(open(path,'rb'))
    return(encode_in(string))
    
    
# testing now    
def main():
    keypath="./tmp/key.pickle"
    e=encode(keypath,"larry")
    print(e)
    
    e1=decode(keypath,e)
    
    print(e1)

main()

