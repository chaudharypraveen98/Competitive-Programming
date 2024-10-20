class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0
        for ch in s:
            if ch == "(":
                left_max += 1
                left_min += 1
            elif ch == ")":
                left_max -= 1
                left_min -= 1
            else:
                left_min -= 1
                left_max += 1
            # it means right parenthesis are more than the left one
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkValidString(
        "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))
