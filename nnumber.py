n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10000
    tot=tot+dig
    n=n//10000
print("The total sum of digits is:",tot)    
