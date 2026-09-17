import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums

        small = []  # max heap
        large = []  # min heap - can have 1 more elements than small
        medians = []
        for j in range(k):
            heapq.heappush(large, (nums[j], j))

        for _ in range(k // 2):
            num = heapq.heappop(large) # move half of the nums from large to small to keep balance
            heapq.heappush(small, (-num[0], num[1]))

        medians.append(self.get_median(small, large, k))

        for i in range(k, len(nums)):
            if nums[i] >= large[0][0]:  # true if nums[k] belongs to large heap
                heapq.heappush(large, (nums[i], i))
                if nums[i - k] <= -small[0][0]:  # means the outgoing number is in small heap, which will be removed soon in the while loop below
                    self.move(large, small)
            else: # goto this branch if nums[i] belongs to small heap
                heapq.heappush(small, (-nums[i], i)) 
                if nums[i - k] >= large[0][0]: # means the outgoing number is in max heap
                    self.move(small, large)

            # # only need to pop the number if the number is at the top of the heap and it is out of the window 
            while large and large[0][1] < (i - k + 1): 
                heapq.heappop(large)
            while small and small[0][1] < (i - k + 1):
                heapq.heappop(small)

            medians.append(self.get_median(small, large, k))

        return medians

    def get_median(self, small, large, k):
        if k % 2 == 1:
            return large[0][0]
        else:
            return (-small[0][0] + large[0][0]) / 2.0

    def move(self, fromHeap, toHeap):
        num, idx = heapq.heappop(fromHeap)
        heapq.heappush(toHeap, (-num, idx))

sol = Solution()
print(sol.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sol.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))
print(sol.medianSlidingWindow([1, 1, 3, 2, 0, 0], 3))
print(sol.medianSlidingWindow([1, 1, 1, 1], 2))
print(sol.medianSlidingWindow([7,8,8,3,8,1,5,3,5,4], 3))
