class Solution:
    def recamanSequence(self, n):
        if n < 2:
            # For n=0 or n=1, the sequence is just [0] or [0, 1] respectively.
            return [i for i in range(n)]

        visited = {0, 1}  # Set to keep track of visited numbers.
        sequence = [0, 1]  # List to store the Recaman sequence.
        current = 1  # Current value in the sequence.

        for i in range(2, n + 1):
            # Calculate the next term in the sequence.
            current = current - i if current - i >= 0 and current - \
                i not in visited else current + i
            visited.add(current)
            sequence.append(current)

        return sequence


if __name__ == '__main__':
    ob = Solution()
    ans = ob.recamanSequence(8)
    for i in range(8):
        print(ans[i], end=" ")
    print()
