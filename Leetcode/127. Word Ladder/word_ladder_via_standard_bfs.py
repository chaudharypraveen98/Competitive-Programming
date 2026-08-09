from collections import deque

class Solution:
    def word_diff_by_1(self,word1, word2):
        is_diff = False
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                if is_diff:
                    return False
                else:
                    is_diff = True
        return True
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        depth = 0
        visited ={beginWord}
        queue = deque([[beginWord]])
        while queue:
            items  = queue.popleft()
            temp_array =[]
            for item in items:
                if item == endWord:
                    return depth+1
                visited.add(item)
                neigbours = [word for word in wordList if word not in visited and self.word_diff_by_1(item, word)]
                for neigbour in neigbours:
                    if neigbour not in visited:
                        visited.add(neigbour)
                        temp_array.append(neigbour)
            if temp_array:
                depth +=1
                queue.append(temp_array)
        return 0




sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) 
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])) 