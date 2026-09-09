import heapq


class MedianFinder:

    def __init__(self):
        # lowers: max-heap (storing negative values to simulate max-heap in Python)
        # Stores the smaller half of the numbers
        self.lowers = []
        # highers: min-heap
        # Stores the larger half of the numbers
        self.highers = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lowers, -num)
        
        if self.lowers and self.highers and (-self.lowers[0]>self.highers[0]):
            val = heapq.heappop(self.lowers)
            heapq.heappush(self.highers, -val)
            
        if len(self.lowers) > len(self.highers)+1:
            val = heapq.heappop(self.lowers)
            heapq.heappush(self.highers, -val)
        elif len(self.highers) > len(self.lowers):
            val = heapq.heappop(self.highers)
            heapq.heappush(self.lowers, -val)

    def findMedian(self) -> float:
        if len(self.lowers)> len(self.highers):
            return float(-self.lowers[0])
        return (-self.lowers[0]+self.highers[0])/2.0


# ==========================================
# DRIVER CODE & HELPERS
# ==========================================

if __name__ == "__main__":
    # Test Case 1: Canonical LeetCode Example
    print("--- Running Test 1 ---")
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    med1 = obj.findMedian()
    print(f"Added [1, 2] -> Median: {med1}")
    assert med1 == 1.5

    obj.addNum(3)
    med2 = obj.findMedian()
    print(f"Added 3 -> Median: {med2}")
    assert med2 == 2.0

    # Test Case 2: Out of order stream with negatives and duplicates
    print("\n--- Running Test 2 ---")
    stream = [5, 15, 1, 3]
    # Sorted views at each step:
    # [5]             -> 5.0
    # [5, 15]         -> 10.0
    # [1, 5, 15]      -> 5.0
    # [1, 3, 5, 15]   -> 4.0
    expected_medians = [5.0, 10.0, 5.0, 4.0]

    finder = MedianFinder()
    for num, expected in zip(stream, expected_medians):
        finder.addNum(num)
        actual = finder.findMedian()
        print(
            f"Added {num:2d} | Median: {actual:4.1f} | Expected: {expected:4.1f}")
        assert actual == expected

    # Test Case 3: LeetCode Command-List Invocation Simulator
    print("\n--- Running Test 3 (Command-Simulator) ---")
    commands = [
        "MedianFinder",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
    ]
    params = [[], [-1], [], [-2], [], [-3], []]
    output = []
    instance = None

    for cmd, param in zip(commands, params):
        if cmd == "MedianFinder":
            instance = MedianFinder()
            output.append(None)
        elif cmd == "addNum":
            instance.addNum(param[0])
            output.append(None)
        elif cmd == "findMedian":
            output.append(instance.findMedian())

    print(f"Commands: {commands}")
    print(f"Output:   {output}")
    assert output == [None, None, -1.0, None, -1.5, None, -2.0]
    print("\nAll assertions passed successfully!")
