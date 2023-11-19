class Solution:
    def finalValueAfterOperations(self, operations):
        x=0
        for op in operations:
            if op=="X++" or op=="++X":
                x+=1
            else:
                x-=1
        return x

    def finalValueAfterOperations1(self, operations):
        x=0
        for op in operations:
            if "+" == op[1]:
                x+=1
            else:
                x-=1
        return x

item  = Solution()
print(item.finalValueAfterOperations(["X++","++X","--X","X--"]))
print(item.finalValueAfterOperations1(["X++","++X","--X","X--"]))