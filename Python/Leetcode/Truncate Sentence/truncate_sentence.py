class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        white_space = 0
        for i in range(len(s)):
            if s[i]==" ":
                white_space+=1
                if white_space==k:
                    return s[:i]
        return s

item  = Solution()
print(item.truncateSentence("Hello how are you Contestant",4))