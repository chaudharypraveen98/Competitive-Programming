class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n is power of 2 if and only if n & n-1 ==0
        return n and not(n&n-1)

sol=Solution()
print(sol.isPowerOfTwo(3))

