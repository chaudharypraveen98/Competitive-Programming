class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left !=right:
            left >>= 1
            right >>= 1
            count +=1
        return left << count
    
    def rangeBitwiseAnd1(self, left: int, right: int) -> int:
        ans = right
        while ans and left < right:
            ans &= left
            left+=1
        return ans

            
    
item  = Solution()
print(item.rangeBitwiseAnd(5,7))
print(item.rangeBitwiseAnd1(5,7))