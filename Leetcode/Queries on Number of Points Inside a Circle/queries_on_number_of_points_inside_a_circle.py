class Solution:
    def countPoints(self, points, queries):
        ans = []
        for query in queries:
            temp=0         
            for point in points:
                distance = abs(query[0]-point[0])**2 + abs(query[1]-point[1])**2
                if distance<= query[2]**2 :
                    temp+=1
            ans.append(temp)
        return ans

item  = Solution()
print(item.countPoints([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]]))
