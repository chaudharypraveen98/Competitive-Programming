#https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly/

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            last_bit = n>>i&1
            ans = ans | last_bit<<(31-i)
        return ans


item  = Solution()
print(item.reverseBits(43261596))