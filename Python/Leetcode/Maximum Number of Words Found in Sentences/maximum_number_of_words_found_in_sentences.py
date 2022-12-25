class Solution:
    def mostWordsFound(self, sentences):
        return max(map(lambda x: len(x.split(" ")),sentences))
item  = Solution()
print(item.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))