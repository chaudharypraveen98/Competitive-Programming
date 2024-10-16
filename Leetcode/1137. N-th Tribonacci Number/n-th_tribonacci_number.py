class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        for i in range(3, n+1):
            arr.append(arr[i-1]+arr[i-2] + arr[i-3])
        return arr[n]

    def recursive(self, n, memo):
        if n in memo:
            return memo[n]
        memo[n] = self.recursive(
            n-1,  memo)+self.recursive(n-2, memo)+self.recursive(n-3, memo)
        return memo[n]

    def tribonacci1(self, n: int) -> int:
        init_arr = {0: 0, 1: 1, 2: 1}
        return self.recursive(n, init_arr)


if __name__ == '__main__':
    sol = Solution()
    print(sol.tribonacci1(0))
