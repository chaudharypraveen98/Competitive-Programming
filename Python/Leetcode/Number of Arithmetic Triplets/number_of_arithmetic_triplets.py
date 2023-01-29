class Solution:
    def arithmeticTriplets(self, nums, diff) -> int:
        hashmap=set()
        res=0
        for i in nums:
            if (i-diff) in hashmap and (i-(2*diff)) in hashmap:
                res+=1
            hashmap.add(i)
        return res

item  = Solution()
print(item.arithmeticTriplets([0,1,4,6,7,10],3))