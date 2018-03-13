def closestNumber(n, m) :
    
    q = n // m
     
    n1 = m * q
     
    if((n * m) > 0) :
        n2 = (m * (q + 1)) 
    else :
        n2 = (m * (q - 1))

    if (abs(n - n1) < abs(n - n2)) :
        return n1
    return n2
n = 13; m = 4
print(closestNumber(n, m))
 
n = -15; m = 6
print(closestNumber(n, m))
 
n = 0; m = 8
print(closestNumber(n, m))
 
n = 18; m = -7
print(closestNumber(n, m))
