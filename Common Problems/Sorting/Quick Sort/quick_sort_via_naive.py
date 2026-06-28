def naive_partitioning(arr, low, high):
    pivot = arr[high]
    temp = []
    ans = 0
    
    # 1. Gather elements less than or equal to pivot
    for i in range(low, high+1):
        if arr[i] <= pivot:
            temp.append(arr[i])
            
    # 2. Gather elements greater than pivot
    for i in range(low, high+1):
        if arr[i] > pivot:
            temp.append(arr[i])
            
    # 3. Copy back to the original array using the 'low' offset
    for i in range(0, len(temp)):
        if temp[i] == pivot:
            ans = low + i
        arr[low + i] = temp[i] 
        
    return ans

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    def _helper(arr, l, h):
        if l<h:
            p = naive_partitioning(arr, l, h)
            _helper(arr, l,p-1)
            _helper(arr,p+1, h)
    _helper(arr, 0, len(arr)-1)
    return arr

array = [3,4,1,5,2,8,6]
print(quick_sort(array))