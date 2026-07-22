class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        stack = set()
        hashmap = {i: [] for i in range(numCourses)}
        for course, req in prerequisites:
            hashmap[course].append(req)

        def is_cyclic(node):
            if node in stack:
                return True
            if node in visited:
                return False
            visited.add(node)
            stack.add(node)
            for dependent_course in hashmap[node]:
                if is_cyclic(dependent_course):
                    return True
            stack.remove(node)
            return False
                
        for course in hashmap:
            if is_cyclic(course):
                return False
        return True
    
sol = Solution()
print(sol.canFinish(2,[[1,0]]))
print(sol.canFinish(2,[[1,0],[0,1]]))
print(sol.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))
print(sol.canFinish(1,[]))
print(sol.canFinish(3,[[1,0],[2,1]]))