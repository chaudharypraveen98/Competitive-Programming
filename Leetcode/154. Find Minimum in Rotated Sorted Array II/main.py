class Solution:
    def findMin(self, nums) -> int:
        def dnc(left, right):
            if(left==right):
                return nums[left]
            if(nums[left]<nums[right]):
                return nums[left]
            
            mid = (left+right)//2
            return min(dnc(left,mid), dnc(mid+1, right))
        return dnc(0, len(nums)-1)
        

# Verification execution pass
sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))  # Output: 1