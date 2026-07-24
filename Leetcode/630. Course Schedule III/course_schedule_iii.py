import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        
        max_heap = []
        total_duration = 0
        
        for duration, last_day in courses:
            total_duration += duration
            heapq.heappush_max(max_heap, duration)
            
            if total_duration > last_day:
                longest_duration = heapq.heappop_max(max_heap)
                total_duration -= longest_duration
                
        return len(max_heap)

sol = Solution()
print(sol.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]]))
print(sol.scheduleCourse([[3,2],[4,3]]))
print(sol.scheduleCourse([[1,2]]))