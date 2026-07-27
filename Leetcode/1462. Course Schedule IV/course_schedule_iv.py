class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courses = {course:[] for course in range(numCourses)}
        for main_course, pre_req in prerequisites:
            courses[main_course].append(pre_req)
        memo = {}
        
        def dfs(node):
            if node in memo:
                return memo[node]
            
            # A node can reach all nodes reachable from its neighbors, plus the neighbors themselves
            reachable = set()
            for neighbor in courses[node]:
                reachable.add(neighbor)
                reachable.update(dfs(neighbor))
                
            memo[node] = reachable
            return memo[node]
        
        for course in courses:
            dfs(course)


        results = []
        for u,v in queries:
            results.append(True if v in memo[u] else False)
        return results
        


sol = Solution()
print(sol.checkIfPrerequisite(2, [], [[1,0],[0,1]]))
print(sol.checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]))
print(sol.checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))