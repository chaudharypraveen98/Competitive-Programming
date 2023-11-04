"""
countAndSay(1) = "1" => countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
countAndSay(5) = say "1211" = one 1's + one 2's + two of 1's = "11"+"12"+"21"= "111211"

what happens is that we have to say the previous number in simpliest way .
- start from res one
- find same consecutive number and resolve to simple like 111 i.e three 1's

"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 2:
            return "1"*n
        res = "11"
        for _ in range(3, n+1):
            j = start = 0
            temp_res = ""
            for j in range(1, len(res)):
                if res[j] != res[j-1]:
                    temp_res += str(j-start)+res[j-1]
                    start = j
                j += 1
            res = temp_res+str(j-start)+res[j-1]
        return res


item = Solution()
print(item.countAndSay(4))

# 9
# Output
# "31131211131221"


# 6
# Output
# "312211"
# Expected
# "312211"
