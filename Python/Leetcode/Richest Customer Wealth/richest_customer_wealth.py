class Solution:
    def maximumWealth(self, accounts):
        return max(map(lambda x: sum(x),accounts))
item  = Solution()
print(item.maximumWealth([[1,5],[7,3],[3,5]]))