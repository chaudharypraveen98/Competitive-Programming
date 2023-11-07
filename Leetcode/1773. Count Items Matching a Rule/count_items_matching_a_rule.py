class Solution:
    def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
        rule_map={
            "type":0,
            "color":1,
            "name":2
        }
        res = 0
        for item in items:
            if item[rule_map[ruleKey]]==ruleValue:
                res+=1
        return res

item  = Solution()
print(item.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],"type","phone"))