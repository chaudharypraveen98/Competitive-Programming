class Solution:
    def shiftPile(self, N, n):
        # code here
        arr = []
        self.towerHanoi(N, "1", "2", "3", arr)
        # print(arr)
        return arr[n-1]

    def towerHanoi(self, N, s, a, d, arr):
        if N == 1:
            arr.append([s, d])
            return
        self.towerHanoi(N-1, s, d, a, arr)
        arr.append([s, d])
        self.towerHanoi(N-1, a, s, d, arr)


if __name__ == '__main__':
    ob = Solution()
    ans = ob.shiftPile(4, 5)
    print(ans[0], ans[1])
