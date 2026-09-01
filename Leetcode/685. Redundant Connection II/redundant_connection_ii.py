from typing import List, Optional, Tuple


class Solution:
    def check_has_cycle(
        self,
        n: int,
        graph: List[List[int]],
        ignore_edge: Optional[Tuple[int, int]] = None,
    ) -> bool:
        """
        Detects directed cycles using standard 3-state DFS coloring:
        0: WHITE (unvisited)
        1: GRAY  (currently visiting / on active recursion stack)
        2: BLACK (fully visited / processed)
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        state = [WHITE] * (n + 1)

        def dfs(u: int) -> bool:
            state[u] = GRAY

            for v in graph[u]:
                # Skip the candidate edge under evaluation
                if ignore_edge and (u, v) == ignore_edge:
                    continue

                # Back-edge to a node currently in the call stack => cycle found
                if state[v] == GRAY:
                    return True

                if state[v] == WHITE:
                    if dfs(v):
                        return True

            state[u] = BLACK
            return False

        for node in range(1, n + 1):
            if state[node] == WHITE:
                if dfs(node):
                    return True

        return False

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]
        in_degrees = [0] * (n + 1)

        # Build graph and record in-degrees
        for u, v in edges:
            graph[u].append(v)
            in_degrees[v] += 1

        # Check if any node has two incoming edges (in-degree == 2)
        node_with_two_parents = -1
        for node in range(1, n + 1):
            if in_degrees[node] == 2:
                node_with_two_parents = node
                break

        if node_with_two_parents != -1:
            # CASE 1 & 2: A node has two parents.
            # Test candidate edges pointing to this node in reverse order.
            for k in range(n - 1, -1, -1):
                u, v = edges[k]
                if v == node_with_two_parents:
                    # If ignoring (u, v) leaves the graph acyclic, it is the redundant edge
                    if not self.check_has_cycle(n, graph, ignore_edge=(u, v)):
                        return [u, v]
        else:
            # CASE 3: Every node has in-degree == 1 (pure directed cycle).
            # Test all edges in reverse order; the first one breaking the cycle is the answer.
            for k in range(n - 1, -1, -1):
                u, v = edges[k]
                if not self.check_has_cycle(n, graph, ignore_edge=(u, v)):
                    return [u, v]

        return []

sol = Solution()
print(sol.findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))
print(sol.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))
print(sol.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]])) #[2,1]
print(sol.findRedundantDirectedConnection([[5,2],[5,1],[3,1],[3,4],[3,5]]))