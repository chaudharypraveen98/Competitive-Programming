def lomuto_partition(arr, low, high):
    i = low - 1
    pivot = arr[high]  # Choosing the last element as pivot
    
    for j in range(low, high):
        if arr[j] < pivot:  # Elements smaller than pivot go to the left
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Place the pivot in its correct sorted position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    # Standard Lomuto returns the index of the pivot
    return i + 1 

arr_to_sort = [4, 2, 8, 1, 3, 7, 5, 6]
print("Original:", arr_to_sort)

# Capture the pivot index
pivot_index = lomuto_partition(arr_to_sort, 0, 7)

print("Partitioned Array:", arr_to_sort)
print("Pivot element (6) is now at index:", pivot_index)