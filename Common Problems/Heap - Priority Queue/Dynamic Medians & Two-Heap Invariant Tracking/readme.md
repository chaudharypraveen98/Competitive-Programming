### Phase 4: Dynamic Medians & Two-Heap Invariant Tracking

#### The Concept

When elements arrive dynamically in a continuous stream and you need to query the running median (or arbitrary percentiles) in O(1) time, maintaining a fully sorted array requires O(N) insertion cost.

Instead, divide the incoming numbers into two dynamically balanced halves using two complementary heaps:

-   **`lowers` (Max-Heap):** Stores the smaller half of all numbers seen so far.
    
-   **`highers` (Min-Heap):** Stores the larger half of all numbers seen so far.
    

### The Invariants to Maintain

To guarantee the median is always accessible at the roots in O(1), maintain two rules on every insertion:

1.  **Order Invariant:**
    
    max(lowers)≤min(highers)
    
    Every element in the lower half must be less than or equal to every element in the upper half. If a newly inserted number violates this, move the top of `lowers` to `highers` (or vice versa).
    
2.  **Balance / Size Invariant:**
    
    len(lowers)−len(highers)∈{0,1}
    
    `lowers` is allowed to hold at most one extra element when the total count of numbers is odd.
    

#### Reading the Running Median:

-   **Odd total elements:** Root of `lowers` (len(lowers)\>len(highers)).
    
-   **Even total elements:** Average of the two roots:
    
    2.0max(lowers)+min(highers)​
    

### Challenge Problem

Implement the canonical two-heap design on your own:

**LeetCode [295: Find Median from Data Stream](../../../Leetcode/295.%20Find%20Median%20from%20Data%20Stream/)**

> Implement the `MedianFinder` class:
> 
> -   `MedianFinder()`: Initializes the `MedianFinder` object.
>     
> -   `void addNum(int num)`: Adds the integer `num` from the data stream to the data structure.
>     
> -   `double findMedian()`: Returns the median of all elements so far. Answers within 10−5 of the actual answer will be accepted.
>     
> 
> **Constraints:**
> 
> -   −105≤num≤105
>     
> -   There will be at least one element in the data structure before calling `findMedian`.
>     
> -   At most 5×104 calls will be made to `addNum` and `findMedian`.
>     

Python

```
class MedianFinder:

  def __init__(self):
    pass

  def addNum(self, num: int) -> None:
    pass

  def findMedian(self) -> float:
    pass
```

Write your implementation for `MedianFinder` when ready.