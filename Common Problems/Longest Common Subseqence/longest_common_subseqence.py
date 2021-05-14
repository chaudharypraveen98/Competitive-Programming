# Bottom up approach with dynamic programming
def lcs(word1, word2):
    length_word1 = len(word1)
    length_word2 = len(word2)

    # initialize memo table with one extra row and col
    array = [[0 for _ in range(length_word2 + 1)] for _ in range(length_word1 + 1)]

    # iterating through both strings
    for row in range(length_word1-1, -1, -1):
        for col in range(length_word2-1, -1, -1):

            # if alphabet matches
            if word1[row] == word2[col]:
                array[row][col] = 1 + array[row + 1][col + 1]
            else:
                # Can't decide to move which pointer to move row or col one. So taking max of both
                array[row][col] = max(array[row+1][col],array[row][col+1])
    return array[0][0]


if __name__ == '__main__':
    word_1 = input()
    word_2 = input()
    print(lcs(word_1, word_2))
