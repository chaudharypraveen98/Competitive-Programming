class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word_end = False
        self.word = None

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        root = TrieNode()

        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word
            curr.is_word_end = True
        memo = {}
        
        def dfs(start):
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]
            
            curr = root
            res = []
            
            for i in range(start, len(s)):
                ch = s[i]

                if ch not in curr.children:
                    break

                curr = curr.children[ch]
                if curr.is_word_end:
                    suffixes = dfs(i+1)
                    for suffix in suffixes:
                        res.append((curr.word+" "+suffix).strip())
            memo[start] = res
            return res
        
        return dfs(0)
    
obj = Solution()
print(obj.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))