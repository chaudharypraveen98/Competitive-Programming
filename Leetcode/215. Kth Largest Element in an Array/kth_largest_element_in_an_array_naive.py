from random import choice
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Quickselect method recursive"""
        pivot = choice(nums)

        greater = [x for x in nums if x > pivot]
        equal = [x for x in nums if x == pivot]
        less = [x for x in nums if x < pivot]

        if k <= len(greater):
            return self.findKthLargest(greater, k)
        elif k > len(greater) + len(equal):
            return self.findKthLargest(less, k - len(greater) - len(equal))
        else:
            return equal[0]
        
sol = Solution()

print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))