a=int(input("enter the number"))
l=[]
count=0
for i in range(0,a):
  b=int(input("enter the number"))
  l.append(b)
  count+=1
if(count%2==0):
  print("yes")
else:
  print("no")
