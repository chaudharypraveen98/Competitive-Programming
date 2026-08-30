## [803. Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/description/)
Before approaching it, you should try [2382. Maximum Segment Sum After Removals](../2382.%20Maximum%20Segment%20Sum%20After%20Removals/)


### Approach
1. Reverse-Time Simulation: Adding elements (Union-Find) is O(alpha(N)), 
   whereas tracking disconnections forward is O(V + E) per hit.
2. Virtual Super-Node (ROOF = 0): Anchors all ceiling connections at row == 0
   into a single master component for instant O(1) stability checks.
3. In-Place Hit Tracking (grid -= 1): Accurately distinguishes original empty 
   cells, single hits, and duplicate hit locations without state corruption.
