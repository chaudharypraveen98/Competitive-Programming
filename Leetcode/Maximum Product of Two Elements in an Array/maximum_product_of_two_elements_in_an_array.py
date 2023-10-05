class Solution:
    def maxProduct(self, nums) -> int:
        max_n, sec_max_n = 0,0
        for i in nums:
            if i>max_n:
                sec_max_n = max_n
                max_n = i
            elif i>sec_max_n:
                sec_max_n=i
        return  (max_n-1)*(sec_max_n-1)
item  = Solution()
print(item.maxProduct([3,4,5,2]))