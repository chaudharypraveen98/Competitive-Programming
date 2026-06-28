def lomuto_partition(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] =  arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    def _helper(arr, l, h):
        if l<h:
            p = lomuto_partition(arr, l, h)
            _helper(arr, l,p-1)
            _helper(arr,p+1, h)
    _helper(arr, 0, len(arr)-1)
    return arr

array = [3,4,1,5,2,8,6]
print(quick_sort(array))