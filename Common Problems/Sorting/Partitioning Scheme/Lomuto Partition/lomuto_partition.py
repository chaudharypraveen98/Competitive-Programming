def lomuto_partition(arr, low, high):
    i = low - 1
    pivot = arr[high-1]
    for j in range(low, high-1):
        if(arr[j]<pivot):
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high-1] = arr[high-1], arr[i+1]
    return arr 

print(lomuto_partition([4,2,8,1,3,7,5,6], 0, 8))