class Solution:
    def decode(self, encoded, first):
        res= [first]
        for num in encoded:
            res.append(num^res[-1])
        return res

item  = Solution()
print(item.decode([1,2,3],1))