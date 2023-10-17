class Solution:
    # using set and combination of all patterns
    def findRepeatedDnaSequences(self, s: str):
        sequence =set()
        repeated =set()
        for i in range(len(s)-9):
            cur_seq = s[i:i+10]
            if cur_seq in sequence:
                repeated.add(cur_seq)
            else:
                sequence.add(cur_seq)
        return [*repeated]
    
    # Using Rabin Karp Method
    def findRepeatedDnaSequences1(self, s: str):
        if len(s)<10:
            return []
        input_coded = []
        for i in s:
            if i=="A":
                input_coded.append(1)
            elif i=="C":
                input_coded.append(2)
            elif i=="G":
                input_coded.append(3)
            else:
                input_coded.append(4)
        len_s = len(s)
        len_p = 10
        hash_val = 0
        base = 4
        hashmap = {}
        res = []
        for i in range(10):
            hash_val = hash_val*base + input_coded[i]
        hashmap[hash_val]=1
        for i in range(1,len_s-9):
            hash_val = hash_val*base - input_coded[i-1]*(base**len_p) +input_coded[i+9]
            hashmap[hash_val] = hashmap.get(hash_val,0)+1
            if hashmap[hash_val] ==2:
                res.append(s[i:i+10])
        return res
    
    def findRepeatedDnaSequences2(self, s: str):
        n2d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        candidates = set()
        duplicates = set()
        cur = 0
        
        for i in range(len(s)):
            # only keep at most 9 letters before the current letter
			# or maybe cur &= (1<<18) -1 and extra first char is removed and space is maintained to accomadate new char
            cur &= (1<<18)-1
            #cur %= 1<<18

            #we need to left shift by 2 which can be acheieved by mutlying by 4 as 1 shift  = mutiple by 2
            cur = cur * 4 + n2d[s[i]]
            # skipping untill we get length 10
            if i < 9:
                continue
            
            if cur in candidates:
                duplicates.add(s[i - 9:i + 1])
            else:
                candidates.add(cur)
        return list(duplicates)

sol =Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(sol.findRepeatedDnaSequences1("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(sol.findRepeatedDnaSequences2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

