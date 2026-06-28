def hoare_partitioning(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        # Move i right while arr[i] < pivot
        while True:
            i += 1
            if arr[i] >= pivot:
                break
                
        # Move j left while arr[j] > pivot
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        
        # If pointers cross, return the partition index
        if i >= j:
            return j
        
        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

# Correct high index is len(arr) - 1, which is 7
arr_to_sort = [4, 2, 8, 1, 3, 7, 5, 6]
print("Original:", arr_to_sort)
partition_index = hoare_partitioning(arr_to_sort, 0, len(arr_to_sort) - 1)
print("Partitioned:", arr_to_sort, "at index:", partition_index)