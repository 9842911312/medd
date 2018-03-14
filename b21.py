import math

def sumofNterm( a , d , b ,r , n ):

	sum = 0

	for i in range(1,n+1):

		sum += ((a + (i -1) * d) *
(b * math.pow(r, i - 1)))

	return int(sum)

a = 5

d = 6

b = 2

r = 2

n = 3

print(sumofNterm(a, d, b, r, n)) 
