#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int):
        res=[]
        for h in range(12):
            for m in range(60):
                if(bin(h).count("1")+bin(m).count("1")==turnedOn):
                    res.append(f"{h}:{m:02d}")
        return res
        
# @lc code=end
sol = Solution()
print(sol.readBinaryWatch(2))
