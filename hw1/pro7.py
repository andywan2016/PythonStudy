def dp(l1,l2):
  i=0
  sum=0
  while True:
    if len(l1)<=i or len(l2)<=i:
      return sum
    else:
      sum=sum+l1[i]*l2[i]	
      i+=1 


def main():
  a=[1,2,3]
  b=[4,5,6,7,8,9]
  print dp(a,b)

main()
