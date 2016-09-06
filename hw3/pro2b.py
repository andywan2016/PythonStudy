# Hello World program in Python
import string


class encrot:
    dig=0
    def __init__(self,digits):
        self.dig=digits
        
    def encode(self,string1):
        if self.dig==0:
            return(string1)
        #if self.dig>0:
        else:
            last=string1[-self.dig:-1]+string1[-1]
            #print(last)
            first=string1[0:-1*self.dig]
            return(last+first)
            
        #else:
            #first=string1[0:self.dig]
            
    

#for testing
def main():
    
    e3=encrot(3)
    print(e3.dig)
    alphabet=string.ascii_lowercase
   # print(alphabet)
    prin=e3.encode(alphabet)
    print(prin)
    em3=encrot(-5)
    print(em3.encode(alphabet))
    
main()