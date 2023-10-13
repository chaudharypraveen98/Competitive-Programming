class Solution:
    def toHex(self, num: int) -> str:
        # handling zero case
        if num==0:
            return "0"
        # 2's complement
        if num<0:
            print(num & (2**32-1),(1<<32)+num)
            # num = (1<<32)+num
            num &= (2**32-1)
        hex_str ="0123456789abcdef"
        hex_digits=""
        while num>0:
            digit = num%16
            hex_digits = hex_str[digit] +hex_digits
            num//=16
        return hex_digits

sol = Solution()
print(sol.toHex(-1))

