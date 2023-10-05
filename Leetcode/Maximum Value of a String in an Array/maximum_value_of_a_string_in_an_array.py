class Solution:
    def maximumValue(self, strs) -> int:
        ans = 0
        for st in strs:
            is_int = True
            for i in st:
                if ord(i)<48 or ord(i)>57:
                    is_int = False
                    break
            if is_int:
                ans = max(int(st),ans)
            else:
                ans = max(len(st),ans)
        return ans
    
    def maximumValueAny(self, strs) -> int:
        ans = 0
        for st in strs:
            contains_str = any(ord(i)<48 or ord(i)>57 for i in st)
            ans = max(len(st),ans) if contains_str else max(int(st),ans)
        return ans
item  = Solution()
print(item.maximumValue(["alic3","bob","3","4","00000"]))
print(item.maximumValueAny(["alic3","bob","3","4","00000"]))