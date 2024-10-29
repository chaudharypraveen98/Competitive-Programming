class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        res = 0
        for i in stones:
            if i in jewels_set:
                res += 1
        return res
