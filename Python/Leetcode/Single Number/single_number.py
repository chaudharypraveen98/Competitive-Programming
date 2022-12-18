
# Importing chain class from itertools
from itertools import chain

class Solution:
    def singleNumber(self, nums) -> int:
        set_num = set()
        for i in nums:
            if i not in set_num:
                set_num.add(i)
            else:
                set_num.remove(i)
        return set_num.pop()

    #xor method
    def singleNumber1(self, nums) -> int:
        xor=0
        for num in nums:
            xor^=num
        return xor


item  = Solution()
print(item.singleNumber([4,1,2,1,2]))
print(item.singleNumber1([4,1,2,1,2]))