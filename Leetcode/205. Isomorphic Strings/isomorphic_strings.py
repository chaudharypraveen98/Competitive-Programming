class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s_to_t = {}
        map_t_to_s = {}
        for i in range(len(s)):
            if (s[i] in map_s_to_t and map_s_to_t[s[i]] != t[i]):
                return False
            if (t[i] in map_t_to_s and map_t_to_s[t[i]] != s[i]):
                return False
            map_s_to_t[s[i]] = t[i]
            map_t_to_s[t[i]] = s[i]
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic("paper", "title"))
    # print(sol.isIsomorphic("badc", "baba"))
