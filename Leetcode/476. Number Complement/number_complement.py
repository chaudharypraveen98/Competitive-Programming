class Solution:
    def findComplement(self, num: int) -> int:
        # XOR can  give us complement but issues are leading zeros so we need to xor untill the number's bit
        total_bits =0
        n=num
        while n!=0:
            n>>=1
            total_bits+=1
        mask = (1<<total_bits) -1
        return mask ^ num

sol = Solution()
print(sol.findComplement(0))