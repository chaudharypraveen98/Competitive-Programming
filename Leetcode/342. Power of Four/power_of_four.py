class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        # it will contain 1 at odd places 
        mask = 0b01010101010101010101010101010101
        # But we have make sure that only 1 exit one time
        one_set_bit = n&n-1==0
        if one_set_bit:
            return mask== mask|n
        return False



sol = Solution()
print(sol.isPowerOfFour(16))