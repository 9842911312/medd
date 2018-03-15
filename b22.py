def largest(arr,n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [100, 34, 4, 654698, 8]
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)
