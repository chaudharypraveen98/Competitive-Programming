class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 0
        suffix = 0
        res = nums[0]
        n = len(nums)
        for i in range(0, len(nums)):
            prefix = (1 if prefix==0 else prefix)*nums[i]
            suffix = (1 if suffix==0 else suffix)*nums[n-1-i]
            res = max(res, prefix, suffix)
            
        return res
    
    def maxProduct1(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        res = nums[0]
        n = len(nums)
        for i in range(1, len(nums)):
            curr = nums[i]
            if(curr<0):
                max_product,min_product = min_product, max_product
            max_product = max(curr, curr*max_product)
            min_product = min(curr, curr*min_product)
            res = max(res, max_product)
            
        return res

item = Solution()
print(item.maxProduct1([2,3,-2,4]))