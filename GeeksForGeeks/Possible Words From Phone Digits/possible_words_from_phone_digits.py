class Solution:
    def __init__(self) -> None:
        self.keypad = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

    def combinations(self, arr, start, path, res):
        if start >= len(arr):
            res.append("".join(path))
            return
        char_list = self.keypad.get(arr[start])
        for i in char_list:
            path.append(i)
            self.combinations(arr, start+1, path, res)
            path.pop()

    # Function to find list of all words possible by pressing given numbers.
    def possibleWords(self, a, N):
        res = []
        self.combinations(a, 0, [], res)
        return res


def main():
    N = 3
    a = [3, 4, 5]
    ob = Solution()
    res = ob.possibleWords(a, N)
    for i in range(len(res)):
        print(res[i], end=" ")

    print()


if __name__ == "__main__":
    main()
