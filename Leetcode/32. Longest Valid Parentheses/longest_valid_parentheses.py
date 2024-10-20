class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                # in case ")("
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i-stack[-1])
        return max_len

    def longestValidParentheses1(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        for i in s:
            if i == "(":
                l += 1
            else:
                r += 1
            if l == r:
                max_len = max(max_len, l*2)
            if r > l:
                l, r = 0, 0
        l, r = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                max_len = max(max_len, l*2)
            if l > r:
                l, r = 0, 0
        return max_len


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses1("()(()"))
