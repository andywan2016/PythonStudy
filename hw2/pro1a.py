def decimals(n):
    def getpivot(num,pivot):
        i=0
        pivot*=10
        while pivot<num:
            pivot*=10
            #yield(0)
            i+=1
        return [pivot,i]
    #def formlist(poi,ls):
       # for x in range(0,poi[1]):
            #ls.append(0)
       # ls.append(poi[0]
    x=1
    first=getpivot(n,1)   
    for k in range(0,first[1]):
        yield(0)

    output1=(first[0]//n)
    yield(output1)
    res=x%n
    
    while True:
        if res is 0:
            return
        else:
            x=getpivot(n,res)
            for j in range(0,x[1]):
                yield(0)
            output1=x[0]//n
            yield(output1)
            res=x[0]%n
        
        
        
def main():
   #a=decimals(18)
   #print(list(a))
   d=decimals(133)
   print([next(d) for x in range(10)])
    
main()

