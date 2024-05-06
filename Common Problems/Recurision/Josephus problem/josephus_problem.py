class Solution:
    def _sub_problem(self, arr, k, prev_ind=0):
        if len(arr) == 1:
            return arr
        ind = prev_ind + k - 1
        if ind >= len(arr):
            ind = ind % len(arr)
        arr.pop(ind)
        return self._sub_problem(arr, k, ind)

    def josephus(self, n, k):
        arr = [i+1 for i in range(n)]
        self._sub_problem(arr, k)
        return arr[0]


# {
 # Driver Code Starts.

def main():
    print(Solution().josephus(3, 2))


if __name__ == "__main__":
    main()
