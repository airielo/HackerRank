n=int(input())
arr=list(map(int, input().split()))

def metrics (n, arr):
   # Mean
    calc_mean=round(sum(arr)/n, 1)
    
    # Median
    sorted_arr=sorted(arr)

    if len(arr)%2==0:
        calc_median=(sorted_arr[n//2]+sorted_arr[n//2-1])/2

    else: 
        calc_median=sorted_arr[(n+1)//2]
    # Mode
    dictionary_mode={}
    for item in arr:
        dictionary_mode[item]=arr.count(item)
    calc_mode=sorted(dictionary_mode.items(), key=lambda x: (x[1], -x[0]))[-1][0]
  
    
    return calc_mean, calc_median, calc_mode
    
calc_mean, calc_median, calc_mode = metrics(n, arr)
print(calc_mean)
print(calc_median)
print(calc_mode)