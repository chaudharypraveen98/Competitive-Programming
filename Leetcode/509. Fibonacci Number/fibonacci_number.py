class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n-1)+self.fib(n-2)

    def fib1(self, n: int) -> int:
        if n < 2:
            return n
        arr = [0, 1]
        for i in range(2, n+1):
            arr.append(arr[i-1]+arr[i-2])
        return arr[n]


item = Solution()
print(item.fib(6))
print(item.fib1(6))
# 6
