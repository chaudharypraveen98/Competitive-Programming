from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        queue = deque([(beginWord, 1)])
        word_len = len(beginWord)
        while queue:
            word, level  = queue.popleft()
            if word == endWord:
                return level
            for i in range(word_len):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i]+ch+word[i+1:]
                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, level+1))
        return 0




sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) 
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])) 