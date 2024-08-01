# It will work but reach time limit
# class Solution:
#     def helper(self, res, n, i=1):
#         if i >= len(res):
#             return True
#         j = i
#         while len(res) > j:
#             el = res.pop(j)
#             if el == n:
#                 return False
#             j = j+i
#         return self.helper(res, n, i+1)

#     def isLucky(self, n):
#         res = [i for i in range(1, n+1)]
#         ans = self.helper(res, n)
#         return ans

class Solution:
    def isLucky(self, number):
        # Iterate through numbers from 2 up to and including 'number'
        for divisor in range(2, number + 1):
            # If 'number' is divisible by 'divisor', it's not a lucky number
            if number % divisor == 0:
                return False
            # If 'divisor' becomes greater than 'number', it's a lucky number
            print(divisor, number)
            if divisor > number:
                return True
            # Update 'number' by subtracting its integer division by 'divisor'
            number -= (number // divisor)
        # If no divisors were found, it's a lucky number
        return True


if __name__ == '__main__':
    obj = Solution()
    if obj.isLucky(19):
        print(1)
    else:
        print(0)
