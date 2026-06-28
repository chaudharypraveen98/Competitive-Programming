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
            ans = low + i  # FIX: Absolute index relative to 'low'
        arr[low + i] = temp[i]  # FIX: Write back to the correct slice of 'arr'
        
    return ans

# Test with your array
arr_to_sort = [4, 6, 8, 1, 3, 7, 5, 2]
print("Original:   ", arr_to_sort)
partition_index = naive_partitioning(arr_to_sort, 0, len(arr_to_sort) - 1)
print("Partitioned:", arr_to_sort, "at index:", partition_index)