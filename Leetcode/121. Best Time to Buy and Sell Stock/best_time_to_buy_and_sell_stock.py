from typing import List


class Solution:
    def calculate(self, idx: int, prices: List[int], min_price: int, max_profit: int) -> int:
        # Base case: if we've reached the end of the price list
        if idx == len(prices):
            return max_profit

        # Update min_price to the lowest so far
        min_price = min(min_price, prices[idx])

        # Calculate profit if we sell at the current price
        current_profit = prices[idx] - min_price

        # Update max_profit if the current profit is higher
        max_profit = max(max_profit, current_profit)

        # Recursive call to process the next day
        return self.calculate(idx + 1, prices, min_price, max_profit)

    def maxProfit(self, prices: List[int]) -> int:
        # Start recursion with the first index, an infinite minimum price, and 0 profit
        return self.calculate(0, prices, float('inf'), 0)

    def maxProfitIterative(self, prices: List[int]) -> int:
        min_price, profit = float('inf'), 0
        for i in prices:
            min_price = min(min_price, i)
            profit = max(profit, i-min_price)
        return profit


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([2, 1, 2, 1, 0, 0, 1]))
