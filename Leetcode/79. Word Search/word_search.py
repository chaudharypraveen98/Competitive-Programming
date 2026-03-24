from collections import Counter

class Solution(object):
    def __init__(self):
        self.direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def search_in_all_direction(self, board, word, visited_board, i=0, j=0):
        if (word == ''):
            return True
        # 4. Boundary Pruning
        if (len(word) > (len(board)*len(board[0]))):
            return False
        if (i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited_board[i][j] or board[i][j] != word[0]):
            return False
        # 2. Using Array to Mark already visited
        visited_board[i][j] = True
        res = any(self.search_in_all_direction(
            board, word[1:], visited_board, i+p, j+q) for p, q in self.direction)
        visited_board[i][j] = False
        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows, cols = len(board), len(board[0])

        # 1. PRUNING: Quick check if word is even possible
        if len(word) > rows * cols:
            return False
        
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
            
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
        visited_board = [[False for _ in range(cols)] for _ in range(rows)]
        # trying word at each index
        for i in range(0, rows):
            for j in range(0, cols):
                if (self.search_in_all_direction(board, word, visited_board,  i, j)):
                    return True
        return False


obj = Solution()
print(obj.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

# ["A","B","C","E"]
# ["S","F","E","S"]
# ["A","D","E","E"]
