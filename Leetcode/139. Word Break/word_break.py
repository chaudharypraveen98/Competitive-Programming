class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class Solution(object):

    def wordBreak(self, s, wordDict):
        # 1. Build the Trie
        root = TrieNode()
        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.isWordEnd = True

        memo = {}

        def dfs(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            
            curr =  root

            for i in range(start, len(s)):
                ch = s[i]

                if ch not in curr.children:
                    break

                curr = curr.children[ch]

                if curr.isWordEnd:
                    if dfs(i+1):
                        memo[start] = True
                        return True
            memo[start] = False
            return False

        return dfs(0)
    
obj = Solution()

print(obj.wordBreak('bb', ["a","b","bbb","bbbb"]))