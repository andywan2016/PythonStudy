def shortlong(tv0,tv1):
  l=[]
  if len(tv0)<len(tv1):
    l=l.append(tv0)
    l=l.append(len(tv0))
    l=l.append(tv1)
    l=l.append(len(tv1))

  else:
    l=l.append(tv1)
    l=l.append(len(tv1))
    l=l.append(tv0)
    l=l.append(len(tv0))

  return l

def main():
  a=[1,2,3]
  b=[4,5,6,7,8,9]
  print shortlong(a,b)

main()
