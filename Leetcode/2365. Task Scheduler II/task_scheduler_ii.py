from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        current_time = 0
        next_available_map ={}
        for task in tasks:
            current_time +=1
            if task in next_available_map and current_time < next_available_map[task]:
                current_time = next_available_map[task]
            next_available_map[task] = space+current_time+1
  
        return current_time
        
    
sol = Solution()
print(sol.taskSchedulerII([1,2,1,2,3,1], 3))
print(sol.taskSchedulerII([5,8,8,5], 2))
