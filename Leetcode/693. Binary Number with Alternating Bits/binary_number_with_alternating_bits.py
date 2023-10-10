class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n and n>>1:
            current_bit = n&1
            if current_bit==n>>1&1:
                return False
            n>>=1
        return True
    def hasAlternatingBits1(self, n: int) -> bool:
        temp = (n>>1) +n
        return (temp&temp+1)==0
sol = Solution()
print(sol.hasAlternatingBits(4))
print(sol.hasAlternatingBits1(4))