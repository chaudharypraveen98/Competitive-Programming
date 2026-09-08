from typing import Any, List, Optional


class MinHeap:

  def __init__(self, arr: Optional[List[Any]] = None) -> None:
    self.heap: List[Any] = list(arr) if arr is not None else []
    if self.heap:
      self._build_up()

  def peek(self) -> Optional[Any]:
    if not self.heap:
      return None
    return self.heap[0]

  def __len__(self) -> int:
    return len(self.heap)

  def push(self, item: Any) -> None:
    self.heap.append(item)
    self._sift_up(len(self.heap) - 1)

  def pop(self) -> Optional[Any]:
    if not self.heap:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()

    min_val = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._sift_down(0)
    return min_val

  def _sift_up(self, index: int) -> None:
    while index > 0:
      parent = (index - 1) // 2
      if self.heap[index] < self.heap[parent]:
        self.heap[index], self.heap[parent] = (
            self.heap[parent],
            self.heap[index],
        )
        index = parent
      else:
        break

  def _sift_down(self, index: int) -> None:
    n = len(self.heap)
    while True:
      smallest = index
      left = 2 * index + 1
      right = 2 * index + 2

      if left < n and self.heap[left] < self.heap[smallest]:
        smallest = left

      if right < n and self.heap[right] < self.heap[smallest]:
        smallest = right

      if smallest != index:
        self.heap[smallest], self.heap[index] = (
            self.heap[index],
            self.heap[smallest],
        )
        index = smallest
      else:
        break

  def _build_up(self) -> None:
    n = len(self.heap)
    last_parent = (n - 2) // 2
    for i in range(last_parent, -1, -1):
      self._sift_down(i)


# 1. Test basic push & pop
h = MinHeap()
for num in [7, 3, 9, 1, 5]:
  h.push(num)

assert h.peek() == 1
assert [h.pop() for _ in range(len(h))] == [1, 3, 5, 7, 9]

# 2. Test O(N) Heapify construction (raw_data remains untouched)
raw_data = [12, 4, 8, 3, 1, 15, 6]
h2 = MinHeap(raw_data)
assert [h2.pop() for _ in range(len(h2))] == [1, 3, 4, 6, 8, 12, 15]
assert raw_data == [12, 4, 8, 3, 1, 15, 6]