from collections import Counter

class Solution(object):
    def __init__(self):
        self.directions = [(1,0),(0,1),(-1,0),(0,-1)]

    def search_at_index(self, board, word, visited, i=0, j=0):
        if(word==''):
            return True
        if i<0 or j <0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j] or visited[i][j]:
            return False
        visited[i][j] = True
        res = any(self.search_at_index(board, word[1:], visited, i+p, j+q) for (p,q) in self.directions)
        visited[i][j] = False
        return res
    
    def search_all_index(self,board, word, visited_board, boards_chars):
        rows = len(board)
        cols = len(board[0])
        if(len(word)> (rows*cols)):
            return False
        # Early prunning
        word_chars = Counter(word)
        for char, count in word_chars.items():
            if count > boards_chars[char]:
                return False

        if word_chars[word[0]] > word_chars[word[-1]]:
            word = word[::-1]

        for i in range(rows):
            for j in range(cols):
                if self.search_at_index(board, word, visited_board, i, j):
                    return True
        return False
        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        visited_board = [[False for _ in board[0]] for _ in board]
        res = []
        boards_chars = Counter(col for row in board for col in row)
        for word in words:
            if self.search_all_index(board, word, visited_board, boards_chars):
                res.append(word)
        return res