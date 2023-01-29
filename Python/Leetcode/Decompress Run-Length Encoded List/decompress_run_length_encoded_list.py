class Solution:
    def decompressRLElist(self, nums):
        generated=[]
        for i in range(0,len(nums),2):
            generated+=[nums[i+1]]*(nums[i])
        return generated

item  = Solution()
print(item.decompressRLElist([1,2,3,4]))