from typing import List

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.count = [0]*n

    def find(self, u: int) -> int:
        root = u
        while self.parent[root] != root:
            root = self.parent[root]
        start = u
        while start != root:
            parent = self.parent[start]
            self.parent[start] = root
            start = parent
        return root

    def union(self, u: int, v: int) -> int:
        parent_u, parent_v = self.find(u), self.find(v)
        if parent_u == parent_v:
            return self.count[parent_u]
        self.parent[parent_v] = parent_u
        self.count[parent_u] += self.count[parent_v]
        return self.count[parent_u]

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n= len(nums)
        union_find = UnionFind(n)
        is_active = [False] * n
        
        # unnionize not required because -> n == nums.length == removeQueries.length
        res = [0]*len(removeQueries)
        current_max = 0
        for k in range(len(removeQueries)-1,-1,-1):
            idx = removeQueries[k]
            is_active[idx] = True
            union_find.count[idx] = nums[idx]
            res[k] = current_max
            current_max = max(current_max, nums[idx])
            
            # Connect to left neighbor if active
            if idx > 0 and is_active[idx - 1]:
                merged_sum = union_find.union(idx, idx - 1)
                current_max = max(current_max, merged_sum)

            # Connect to right neighbor if active
            if idx < n - 1 and is_active[idx + 1]:
                merged_sum = union_find.union(idx, idx + 1)
                current_max = max(current_max, merged_sum)
        return res
      
sol = Solution()      
print(sol.maximumSegmentSum([1,2,5,6,1], [0,3,2,4,1]))
print(sol.maximumSegmentSum([3,2,11,1], [3,2,1,0]))