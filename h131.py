j=input()
data=sorted(map(int,raw_input().split(" ")))
rev=data[::1]
tmp=reduce(lambda x1,x2:x1+x2,[[data[-i],rev[-i]] for i in range(1,j/2+1)])
if j%2==0:
  print " ".join(map(str,tmp))
else:
  print " ".join(map(str,tmp)),data[-(j/2+1)]
