from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        begin_set = {beginWord}
        end_set = {endWord}
        level = 1
        while begin_set and end_set:
            if len(begin_set)>len(end_set):
                begin_set, end_set = end_set, begin_set
            temp_begin_set = set()
            for word in begin_set:
                for i in range(len(beginWord)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        next_word = word[:i]+ch+word[i+1:]
                        if next_word in end_set:
                            return level +1
                        if next_word in word_set:
                            word_set.remove(next_word)
                            temp_begin_set.add(next_word)
            level +=1
            begin_set = temp_begin_set
        return 0

sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) 
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])) 