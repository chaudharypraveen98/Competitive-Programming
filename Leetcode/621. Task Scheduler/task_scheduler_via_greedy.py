from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        max_freq = freq[25]
        gaddhe = max_freq - 1
        idle_slots = gaddhe * n
        
        for idx in range(24, -1,-1):
            idle_slots -= min(freq[idx], gaddhe)
        
        if idle_slots >0:
            return len(tasks)+idle_slots
        return len(tasks)
        
            
    
sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))
print(sol.leastInterval(["A","C","A","B","D","B"], 1))
print(sol.leastInterval(["A","A","A", "B","B","B"], 3))
print(sol.leastInterval(["A","B","C","D","E","A","B","C","D","E"],4))