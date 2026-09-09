### The Inverted Boundary Rule

The fundamental intuition for Top-K problems is counter-intuitive:

-   To find the **$K$ Largest** elements, maintain a **Min-Heap** of size $K$.
-   To find the **$K$ Smallest** elements, maintain a **Max-Heap** of size $K$.

#### Why Invert?

If you use a Max-Heap to track the $K$ largest elements, the largest number sits at the root (`heap[0]`). When a new element arrives, you have to compare it against the maximum, which forces you to store all $N$ elements ($O(N)$ space and $O(N \\log N)$ total time).

With a **Min-Heap of size $K$**:

1.  The root (`heap[0]`) holds the **smallest of the top-$K$ candidates seen so far** (the threshold to beat).
2.  For each incoming number:
    -   If `len(heap) < k`: push it.
    -   If `val > heap[0]`: pop the current minimum threshold and push `val` (or use `heapreplace`).
3.  After scanning all $N$ numbers, the heap retains strictly the $K$ largest elements.
4.  **Complexity:** $O(N \\log K)$ time and $O(K)$ space.
   

### Some Problems
1. [215. Kth Largest Element in an Array](../../../../Leetcode/215.%20Kth%20Largest%20Element%20in%20an%20Array/)