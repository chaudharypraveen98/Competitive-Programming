from math import floor
import sys
sys.setrecursionlimit(10**8)


class Solution:
    # Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        mid = floor((sizeOfStack+1)/2)
        if mid == len(s):
            s.pop()
            return s
        top = s.pop()
        self.deleteMid(s, sizeOfStack)
        s.append(top)
        return s


if __name__ == "__main__":
    sol = Solution()
    print(sol.deleteMid([1, 2, 3, 4, 5],5))