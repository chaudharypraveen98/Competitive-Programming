class Solution:
    def largestAltitude(self, gain) -> int:
        ans,sum_all = 0,0
        for i in gain:
            sum_all+=i
            ans=max(sum_all,ans)
        return ans

item  = Solution()
print(item.largestAltitude([-5,1,5,0,-7]))