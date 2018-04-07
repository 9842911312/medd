a=input(" enter the n number")
b=input(" enter the k number")\
c=list(str(a))
e=b
while e>0:
  e=e-1
  del(c[e])
print(' ',join(c))  
