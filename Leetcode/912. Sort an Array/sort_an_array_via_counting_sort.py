def couting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_el = max_val-min_val+1
    count_arr = [0]*range_of_el
    output_arr = [0]*len(arr)

    # counting each number occurances
    for num in arr:
        count_arr[num-min_val]+=1
    
    # shifting by 1 place to get slots before any number
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # now starting filling from back
    for num in reversed(arr):
        output_arr[count_arr[num-min_val]-1] = num
        count_arr[num-min_val] -= 1

    return output_arr
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        return couting_sort(nums)