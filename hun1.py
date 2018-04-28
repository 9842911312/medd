n=int(input("enter n"))
l=[]
l1=[]
b=0
for i in range(n):
  a=int(input())
  l.append(a)
for i in range(n):
  b=l.count(l[i])
  ifb=2:
    l1.append(l[i])
l1.sort()
s=set(l1)
if len(s)!=0:
  print(s)
else:
  print("unique")
  
