def harmonicMean(arr, n) :
    sm = 0
    for i in range(0, n) :
        sm = sm + (1) / arr[i];
  
    return n / sm
arr = [ 13.5, 14.5, 14.8, 15.2, 16.1 ];
n = len(arr)
print(harmonicMean(arr, n))
