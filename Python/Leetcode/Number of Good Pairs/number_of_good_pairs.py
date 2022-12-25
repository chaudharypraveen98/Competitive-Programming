class Solution:
    # This method is useful if we want to return the index pairs too
    def numIdenticalPairs(self, nums):
        # it contains the value as key and index list as the value
        hash_set = {}
        res=0
        for i in range(len(nums)):
            # checks if value present and increment the index list
            if nums[i] in hash_set:
                res+=len(hash_set[nums[i]])
                hash_set[nums[i]].append(i)
            else:
                hash_set[nums[i]]=[i]
        return res
    
    # it doesn't contains the index list but just the count
    def numIdenticalPairs1(self, nums):
        hash_set = {}
        res=0
        for i in range(len(nums)):
            if nums[i] in hash_set:
                res+=hash_set[nums[i]]
                hash_set[nums[i]]+=1
            else:
                hash_set[nums[i]]=1
        return res
item  = Solution()
print(item.numIdenticalPairs1([1,2,3,1,1,3]))