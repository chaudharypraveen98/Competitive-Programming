from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        begin_set = {beginWord}
        end_set = {endWord}

        is_found = False
        is_reversed = False
        parents = defaultdict(list)
        while begin_set and end_set and not is_found:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
                is_reversed = not is_reversed
            word_set -= begin_set
            temp_begin_set = set()

            for word in begin_set:
                for i in range(len(beginWord)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        next_word = word[:i]+ch+word[i+1:]
                        p,c =(next_word, word) if is_reversed else (word, next_word)
                        if next_word in end_set:
                            is_found = True
                            parents[c].append(p)
                        elif not is_found and next_word in word_set:
                            temp_begin_set.add(next_word)
                            parents[c].append(p)
            begin_set = temp_begin_set
        if not is_found:
            return []

        memo = {}
        print(parents)
        def get_paths(node):
            if node==beginWord:
                return [[beginWord]]
            if node in memo:
                return memo[node]
            res = []
            for parent in parents[node]:
                for path in get_paths(parent):
                    res.append(path+[node])
            memo[node] = res
            return res
        
        return get_paths(endWord)


sol = Solution()
print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])) 
print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])) 