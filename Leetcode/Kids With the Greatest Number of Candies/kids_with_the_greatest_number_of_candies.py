class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)
        #get the total candy by suming extra candies and comparing to max
        return list(map(lambda x:x+extraCandies>=max_candy,candies))
item  = Solution()
print(item.kidsWithCandies([2,3,5,1,3],3))