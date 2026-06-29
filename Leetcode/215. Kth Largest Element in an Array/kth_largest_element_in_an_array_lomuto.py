def partition(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j]<=pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kthIndex = len(nums)-k
        low = 0
        high = len(nums)-1
        while True:
            pivot = partition(nums, low, high)
            if pivot==kthIndex:
                return nums[kthIndex]
            elif kthIndex<=pivot:
                high = pivot-1
            else:
                low = pivot+1

sol = Solution()

print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))