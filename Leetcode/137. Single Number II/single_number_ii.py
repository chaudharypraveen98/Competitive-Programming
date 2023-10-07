#https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly/

class Solution:
    def singleNumber(self, nums):
        ans = 0
        # It will iterate 32 bits [right shift the bites and adding them]
        for i in range(32):
            #It will store the sum at particular position/index in 32 bit number
            bit_sum = 0
            for num in nums:
                # Convert the number to two's complement representation to handle large test case 
                if num < 0:
                    num &= (2**32-1)
                # It will right shift and make logical & to find the last bit
                bit_sum += (num >> i) & 1
            # It is used to find the unbalanced bit at each position
            bit_sum %= 3
            # We will left shift and make logical OR
            ans |= bit_sum << i

        # Convert the result back to two's complement representation if it's negative to handle large test case
        if ans >= 2**31:
            ans -= 2**32

        return ans


item  = Solution()
print(item.singleNumber([-1999,4,3,2,-1999,2,3,2,3,-1999]))