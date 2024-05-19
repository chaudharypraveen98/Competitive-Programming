class Solution:
    ans = []

    def recur(self, n):
        self.ans.append(n)
        if n == 1:
            return
        if n % 2 == 0:
            n = int(n**0.5)
            self.recur(n)
        else:
            n = int(n**1.5)
            self.recur(n)

    def jugglerSequence(self, n):
        self.recur(n)
        return self.ans


if __name__ == '__main__':
    ob = Solution()
    arr = ob.jugglerSequence(14)
    for i in (arr):
        print(i, end=" ")
    print()
