def hoare_partition(arr, low, high):
    i = low-1
    pivot = arr[low]
    j = high+1
    while True:
        while True:
            i+=1
            if arr[i]>=pivot:
                break

        while True:
            j-=1
            if arr[j] <=pivot:
                break

        if i>=j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    def _helper(arr, l, h):
        if l<h:
            p = hoare_partition(arr, l, h)
            _helper(arr, l,p)
            _helper(arr,p+1, h)
    _helper(arr, 0, len(arr)-1)
    return arr

array = [3,4,1,5,2,8,6]
print(quick_sort(array))