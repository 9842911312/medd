n=int(input("Enter The Number:"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverseof the number:",rev)
