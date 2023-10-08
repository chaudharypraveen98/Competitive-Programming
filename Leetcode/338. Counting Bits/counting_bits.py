class Solution:
    def countBits(self, n: int):
        ans =[]
        for i in range(n+1):
            count =0
            while i>0:
                i &=i-1
                count +=1
            ans.append(count)
        return ans

item  = Solution()
print(item.countBits(5))