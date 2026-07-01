def counting_sort(arr):
    if not arr:
        return arr
        
    # 1. Find both min and max to handle negative numbers
    min_val = min(arr)
    max_val = max(arr)
    
    # 2. Determine the exact range size needed
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # 3. Shift each number by subtracting min_val to safely map to index
    for num in arr:
        count_arr[num - min_val] += 1
    
    # 4. Prefix sum accumulation
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # 5. Fill output array from the back (using shifted indices)
    for num in reversed(arr):
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1

    return output_arr

print(counting_sort([5,1,1,2,0,0]))