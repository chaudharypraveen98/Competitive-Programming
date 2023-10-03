class Solution:
    # Converting binary strings to numbers, add them , then return binary of res
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    # manual & iterative method
    def addBinary1(self, a: str, b: str) -> str:
        len_a = len(a)-1
        len_b = len(b)-1
        carry = 0
        res = ""
        while (len_a >= 0 or len_b >= 0 or carry):
            if len_a >= 0:
                carry += int(a[len_a])
                len_a -= 1
            if len_b >= 0:
                carry += int(b[len_b])
                len_b -= 1
            res = str(carry % 2) + res
            carry = carry//2
        return res


item = Solution()
print(item.addBinary("1010", "1011"))
print(item.addBinary1("1010", "1011"))
