## The Active-State Scanner (Two-Pointer / Two-Collection Pattern)
 You have items with two constraints (e.g., start_time vs. end_time, or capital_required vs. profit).

### The Heap Mechanism:
- Sort the items statically by the eligibility threshold (e.g., start time, arrival time, capital).
- Use a Heap to manage the currently eligible/active choices prioritized by the optimization goal (e.g., earliest finish time, shortest job duration, maximum profit)
- Advance time or state, transfer newly unlocked items into the heap, and pop the optimal candidate.

### Challenge Problem

[**Meeting Room II**](../../../../Leetcode/253.%20Meeting%20Rooms%20II/)

> Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the _minimum number of conference rooms required_.
> 
> **Example 1:**
> 
> Plaintext
> 
> ```
> Input: intervals = [[0,30],[5,10],[15,20]]
> Output: 2
> ```
> 
> **Example 2:**
> 
> Plaintext
> 
> ```
> Input: intervals = [[7,10],[2,4]]
> Output: 1
> ```
