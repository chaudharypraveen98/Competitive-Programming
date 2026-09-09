### Phase 3: Multi-Way Merging & K\-Way Pointers

#### The Concept

When consolidating multiple pre-sorted sequences or navigating sorted coordinate spaces, storing all items requires O(NlogN) sorting time.

Instead, maintain a Min-Heap bounded to the number of active streams (K). At any moment, the heap holds only the current frontier element from each sequence:

1.  Initialize the Min-Heap with the first item of each stream along with its coordinates/pointers: `(value, stream_index, element_index)`.
    
2.  Extract the minimum element from the heap and append it to the result.
    
3.  Advance the pointer in the stream that supplied the extracted element, pushing its next value into the heap.
    
4.  Repeat until all streams are drained.
    

This bounds auxiliary space to O(K) and runs in O(NlogK) time, where N is the total count of elements across all K streams.

### Challenge Problem

Try solving this canonical problem on your own first:

**[LeetCode 23: Merge k Sorted Lists](../../../Leetcode/23.%20Merge%20k%20Sorted%20Lists/)**

> You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.
> 
> _Merge all the linked-lists into one sorted linked-list and return it._
> 
> **Example:**
> 
> Plaintext
> 
> ```
> Input: lists = [[1,4,5],[1,3,4],[2,6]]
> Output: [1,1,2,3,4,4,5,6]
> ```

Share your code or approach when ready.