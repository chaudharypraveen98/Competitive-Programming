class Solution:
    def restoreString(self, s: str, indices) -> str:
        res=[" " for i in range(len(s))]
        for i,j in enumerate(indices):
            res[j]=s[i]
        return "".join(res)

    #cyclic sort https://leetcode.com/problems/shuffle-string/solutions/755923/used-cyclic-sort-with-o-1-space-and-o-n-time-complexity/

item  = Solution()
print(item.restoreString("codeleet",[4,5,6,7,0,2,1,3]))