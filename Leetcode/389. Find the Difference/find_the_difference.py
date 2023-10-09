class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans =0
        for i in s:
            ans ^=ord(i)
        for j in t:
            ans ^=ord(j)
        return chr(ans) 
        
    def findTheDifference1(self, s: str, t: str) -> str:
        s_sum,t_sum = 0,0
        for i in s:
            s_sum+=ord(i)
        for j in t:
            t_sum+=ord(j)
        return chr(t_sum-s_sum) 
    

sol = Solution()
print(sol.findTheDifference("abcd","abcde"))
print(sol.findTheDifference1("abcd","abcde"))