import heapq
from typing import List


class Interval(object):

  def __init__(self, start: int, end: int):
    self.start = start
    self.end = end

  def __repr__(self) -> str:
    return f"Interval({self.start}, {self.end})"


class Solution:

  def minMeetingRooms(self, intervals: List[Interval]) -> int:
    if not intervals:
      return 0

    # 1. Sort intervals by start time
    intervals.sort(key=lambda x: x.start)

    # 2. Min-heap stores the end times of rooms currently in use
    heap = []

    for interval in intervals:
      start, end = interval.start, interval.end

      # If the earliest ending meeting finishes before/at this meeting's start time,
      # reuse that room by popping its previous end time
      if heap and start >= heap[0]:
        heapq.heappop(heap)

      # Allocate/extend the room with the new meeting's end time
      heapq.heappush(heap, end)

    # The number of active rooms maintained in the heap is the minimum required
    return len(heap)


# ==========================================
# DRIVER CODE
# ==========================================
if __name__ == "__main__":
  sol = Solution()

  # Test Case 1: Overlapping intervals -> Expected: 2
  raw1 = [(0, 40), (5, 10), (15, 20)]
  intervals1 = [Interval(s, e) for s, e in raw1]
  ans1 = sol.minMeetingRooms(intervals1)
  print(f"Test 1: {ans1} (Expected: 2)")
  assert ans1 == 2

  # Test Case 2: Single interval -> Expected: 1
  raw2 = [(4, 9)]
  intervals2 = [Interval(s, e) for s, e in raw2]
  ans2 = sol.minMeetingRooms(intervals2)
  print(f"Test 2: {ans2} (Expected: 1)")
  assert ans2 == 1

  # Test Case 3: Back-to-back meetings (start == end can reuse the room) -> Expected: 1
  raw3 = [(1, 5), (5, 10), (10, 15)]
  intervals3 = [Interval(s, e) for s, e in raw3]
  ans3 = sol.minMeetingRooms(intervals3)
  print(f"Test 3: {ans3} (Expected: 1)")
  assert ans3 == 1

  # Test Case 4: Fully concurrent meetings -> Expected: 3
  raw4 = [(1, 10), (2, 9), (3, 8)]
  intervals4 = [Interval(s, e) for s, e in raw4]
  ans4 = sol.minMeetingRooms(intervals4)
  print(f"Test 4: {ans4} (Expected: 3)")
  assert ans4 == 3

  print("\nAll tests passed!")