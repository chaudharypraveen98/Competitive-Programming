class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashmap = {};
        seen = set()
        def process(num):
            if num==1:
                return True
            if num in hashmap:
                return hashmap[num]
            if num in seen:
                return False
            seen.add(num)
            sum_num = 0
            temp = num
            while temp>=10:
                mod = temp%10
                temp = temp//10
                sum_num += mod**2
            sum_num += temp**2
            ans =  process(sum_num)
            hashmap[num] = ans
            return ans
        return process(n)
        

item = Solution()
print(item.isHappy(2))