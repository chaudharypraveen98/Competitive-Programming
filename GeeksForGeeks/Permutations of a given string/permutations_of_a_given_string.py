class Solution:
    def helper(self, options, path, res):
        if len(options) < 1:
            item_str = "".join(path)
            if item_str not in res:
                res.add(item_str)
        for i in range(len(options)):
            path.append(options[i])
            self.helper(options[0:i]+options[i+1:], path, res)
            path.pop()
        return res

    def find_permutation(self, S):
        res = self.helper(list(S), [], set())
        return list(res)


if __name__ == '__main__':
    S = "ABSG"
    ob = Solution()
    ans = ob.find_permutation(S)
    ans.sort()
    for i in ans:
        print(i, end=" ")
    print()
    # result
    # ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA
