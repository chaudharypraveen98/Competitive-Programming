## [2382. Maximum Segment Sum After Removals](https://leetcode.com/problems/maximum-segment-sum-after-removals/description/)

### Approach

-   **Reverse-Time Simulation:** Deleting segments splits components (O(N) graph traversal). Running queries in reverse means **inserting elements** and merging components via **Disjoint Set Union (DSU)** in near O(1) time.
    
-   **Permutation Guarantee:** `removeQueries` is a complete permutation of all indices 0…n−1. After all removals, the array is completely empty. No upfront DSU construction is needed.
    
-   **Running Max Tracking:** Never use `max(dsu.totals)` (O(N) scan per query →O(N2) TLE). Maintain a running `current_max` scalar updated in O(1) during merges.
    

### Step-by-Step Algorithm

1.  Initialize empty DSU with `parent` array and component sum array `total`.
    
2.  Initialize an active tracker `is_active = [False] * n` and `current_max = 0`.
    
3.  Iterate queries in **reverse** from k\=n−1 down to 0:
    
    -   **Record Result:** `res[k] = current_max` (the max segment sum _before_ this restoration).
        
    -   **Activate Node:** Set `is_active[idx] = True` and initialize `total[idx] = nums[idx]`.
        
    -   **Update Baseline Max:** `current_max = max(current_max, nums[idx])`.
        
    -   **Merge Left:** If `idx > 0` and `is_active[idx - 1]`:
        
        -   `merged_sum = union(idx, idx - 1)`
            
        -   `current_max = max(current_max, merged_sum)`
            
    -   **Merge Right:** If `idx < n - 1` and `is_active[idx + 1]`:
        
        -   `merged_sum = union(idx, idx + 1)`
            
        -   `current_max = max(current_max, merged_sum)`
            
4.  Return `res`.
    
### Common Pitfalls to Avoid

-   ❌ **Mutating Original `nums` Array Upfront:** Zeroing out `nums` before the reverse loop destroys the reference values needed to populate `uf.total[idx]`.
    
-   ❌ **Global `max()` Scans:** Calling `max(uf.total)` inside the loop turns an O(N⋅α(N)) solution into O(N2) TLE.
    
-   ❌ **Recording `res[k]` After Union:** `res[k]` represents the max segment sum **after the removal** (which equals the state **before the restoration**). Always set `res[k] = current_max` before running unions for `idx`.
    

### Complexity Profile

-   **Time Complexity:** O(N⋅α(N))≈O(N) (Each element is activated and merged at most twice).
    
-   **Space Complexity:** O(N) (DSU `parent`, `total`, and `is_active` arrays).