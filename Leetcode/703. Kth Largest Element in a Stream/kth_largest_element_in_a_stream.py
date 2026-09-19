from heapq import heappush, heappop, heapify
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.right_min = nums
        self.k = k
        heapify(self.right_min)
        while len(self.right_min)>k:
            heappop(self.right_min)

    def add(self, val: int) -> int:
        heappush(self.right_min, val)
        if len(self.right_min)>self.k:
            heappop(self.right_min)
        return self.right_min[0]


def transform_input(input_data):
    """Convert a LeetCode-style sequence into actual outputs."""
    if not input_data or input_data[0] != "KthLargest":
        raise ValueError("Input must start with 'KthLargest'.")

    k, nums = input_data[1]
    kth_largest = KthLargest(k, nums)
    outputs = [None]

    for i in range(2, len(input_data), 2):
        op = input_data[i]
        value = input_data[i + 1][0]

        if op == "add":
            outputs.append(kth_largest.add(value))
        else:
            raise ValueError(f"Unsupported operation: {op}")

    return outputs


if __name__ == "__main__":
    print(transform_input(["KthLargest", [5, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]], "add", [55], "add", [45], "add", [65], "add", [35], "add", [25], "add", [15], "add", [85], "add", [95], "add", [105], "add", [115], "add", [5], "add", [75], "add", [85], "add", [95], "add", [105]]))