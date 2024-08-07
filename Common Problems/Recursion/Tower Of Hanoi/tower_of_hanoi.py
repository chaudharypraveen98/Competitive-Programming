import math

class Solution:
    cnt = 0

    def toh(self, N, fromm, to, aux):
        if N == 1:
            print("move disk", N, "from rod", fromm, "to rod", to)
            self.cnt += 1
            return self.cnt
        self.toh(N-1, fromm, aux, to)
        self.cnt += 1
        print("move disk", N, "from rod", fromm, "to rod", to)
        self.toh(N-1, aux, to, fromm)
        return self.cnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.toh(3, 1, 3, 2))
