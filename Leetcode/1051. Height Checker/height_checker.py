class Solution:
    # Simple For loop
    def heightChecker(self, heights) -> int:
        new_arr = sorted(heights)
        ans=0
        for i in range(len(heights)):
            if new_arr[i]!=heights[i]:
                ans+=1
        return ans
    
    # Use of lamdba and Map
    def heightCheckerLambda(self, heights) -> int:
        new_arr = sorted(heights)
        return sum(map(lambda a,b:a!=b,new_arr,heights))
    
    # Use of Generator Function
    def heightCheckerGenerator(self, heights) -> int:
        new_arr = sorted(heights)
        return sum(1 for i in range(len(heights)) if new_arr[i]!=heights[i])
    
item  = Solution()
print(item.heightChecker([1,1,4,2,1,3]))
print(item.heightCheckerLambda([1,1,4,2,1,3]))
print(item.heightCheckerGenerator([1,1,4,2,1,3]))