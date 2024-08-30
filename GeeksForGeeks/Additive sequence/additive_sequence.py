class Solution:
    def helper(self, s, seq_no, str_index, memo):
        if seq_no in memo:
            return memo[seq_no]
        if str_index >= len(s):
            return 1

        additive_sum = memo[seq_no-1] + memo[seq_no-2]
        end_index = str_index+len(str(additive_sum))
        cur_sum = int(s[str_index:end_index])
        if additive_sum != cur_sum:
            return 0
        memo[seq_no] = additive_sum
        return self.helper(s, seq_no+1, end_index, memo)

    def isAdditiveSequence(self, n):
        max_len = len(s)//3
        for i in range(1, max_len+1):
            next_max_len = len(s[i:])//2
            for j in range(i, next_max_len+1):
                memo = {0: int(s[0:i]), 1: int(s[i:i+j])}
                if self.helper(s, 2, i+j, memo):
                    return 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    s = "12122436"
    print(sol.isAdditiveSequence(s))
