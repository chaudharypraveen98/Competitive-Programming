from collections import Counter, deque
from heapq import heapify, heappop, heappush
from typing import List


class Solution:

  def leastInterval(self, tasks: List[str], n: int) -> int:
    # 1. Frequency counting
    counts = Counter(tasks)

    # 2. Max-heap of remaining counts (using negative values)
    heap = [-cnt for cnt in counts.values()]
    heapify(heap)

    # Queue stores: (available_time, remaining_negative_count)
    task_queue = deque()
    current_time = 0

    while heap or task_queue:
      # If a task's cooldown period is over, push it back to the heap
      if task_queue and task_queue[0][0] == current_time:
        _, rem_count = task_queue.popleft()
        heappush(heap, rem_count)

      # Execute the most frequent available task
      if heap:
        rem_count = heappop(heap) + 1  # Since it's negative, adding 1 decreases absolute count
        if rem_count != 0:
          # Eligible to run again at current_time + n + 1
          task_queue.append((current_time + n + 1, rem_count))

      current_time += 1

    return current_time
            
    
sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))
print(sol.leastInterval(["A","C","A","B","D","B"], 1))
print(sol.leastInterval(["A","A","A", "B","B","B"], 3))
print(sol.leastInterval(["A","B","C","D","E","A","B","C","D","E"],4))