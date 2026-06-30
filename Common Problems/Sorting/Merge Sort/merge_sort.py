def merge(arr1, arr2):
    i,j=0,0
    sorted_arr = []
    while i<len(arr1) and j< len(arr2):
        if arr1[i]<arr2[j]:
            sorted_arr.append(arr1[i])
            i+=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
    sorted_arr.extend(arr1[i:])
    sorted_arr.extend(arr2[j:])
    return sorted_arr

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    left_sorted = merge_sort(arr1)
    right_sorted = merge_sort(arr2)
    return merge(left_sorted, right_sorted)

print(merge_sort([3,4,1,5,2,8,6]))