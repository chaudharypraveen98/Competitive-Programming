class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        max_step = len(s)//2
        for step in range(1,max_step+1):
            step_val = s[0:step]
            temp = True
            for val in range(step, len(s), step):
                if(s[val:val+step] != step_val):
                    temp = False
                    break
            if(temp):
                return True
        return False


sol = Solution()
print(sol.repeatedSubstringPattern("abcabcabcabc"))
print(sol.repeatedSubstringPattern("abab"))
print(sol.repeatedSubstringPattern("aba"))
print(sol.repeatedSubstringPattern("aa"))
print(sol.repeatedSubstringPattern("a"))
print(sol.repeatedSubstringPattern("ababab"))