"""form a rectangle with given stics of lengths given which forms max area"""

def rectangle(n_stks,lengths): 
    arr=[]
    for stk in lengths:
        if lengths.count(stk)>=2 and stk not in arr:
            arr.append(stk)
    max_area =0
    for i in range( len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j] > max_area:
                max_area =  arr[i]*arr[j]
    return max_area 
print(rectangle(5,[1,5,8,5,8]))