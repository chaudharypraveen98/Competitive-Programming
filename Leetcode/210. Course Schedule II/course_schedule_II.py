class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {i:[] for i in range(numCourses)}
        for main_course, pre_req in prerequisites:
            hashmap[main_course].append(pre_req)
        visited = set()
        req_stack = set()
        res = []

        def is_cycle(node):
            if node in req_stack:
                return True
            if node in visited:
                return False

            visited.add(node)
            req_stack.add(node)
            for pre_req in hashmap[node]:
                if is_cycle(pre_req):
                    return True
            res.append(node)
            req_stack.remove(node)
            return False

        for course in hashmap:
            if is_cycle(course):
                return []
        return res



sol = Solution()
# print(sol.findOrder(2,[[1,0]]))
# print(sol.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
print(sol.findOrder(2, [[0,1],[1,0]]))