from pro1a import decimals

def genlimit(g,limit):
    return [next(g) for x in range(limit)]



def main():
    ls=genlimit(decimals(3),5)
    print(list(ls))

main()



    

