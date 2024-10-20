class Solution:
    def isValid(self, s: str) -> bool:
        opening = set(["(", "{", "["])
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for ch in s:
            if ch in opening:
                stack.append(ch)
            else:
                if stack and pairs[ch] == stack[-1]:
                    stack.pop()
                elif len(stack) != 0:
                    stack.append(ch)
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("(]"))
