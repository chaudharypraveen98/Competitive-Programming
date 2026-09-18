from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        result = []
        heap = []
        for i in range(0,min(k, len(nums1))):
            heappush(heap,(nums1[i]+nums2[0], i, 0))
        while heap:
            if len(result)==k:
                return result
            _, idx1, idx2 =  heappop(heap)
            result.append([nums1[idx1], nums2[idx2]])
            if idx2+1 < len(nums2):
                heappush(heap,(nums1[idx1]+nums2[idx2+1], idx1, idx2+1))
        return result



sol = Solution()
print(sol.kSmallestPairs([1,7,11], [2,4,6], 3))
print(sol.kSmallestPairs([1,1,2], [1,2,3], 2))
print(sol.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3))
print(sol.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 20))