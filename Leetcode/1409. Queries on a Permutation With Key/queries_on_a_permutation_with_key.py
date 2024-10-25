from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        process = [i+1 for i in range(m)]
        res = []
        for i in range(len(queries)):
            val = queries[i]
            process_idx = process.index(val)
            print(process_idx)
            res.append(process_idx)
            process.insert(0, process.pop(process_idx))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.processQueries([3, 1, 2, 1], 5))
