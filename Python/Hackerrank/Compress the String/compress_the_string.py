# 1222311
s = input()
i = 0
ans = []
while i < len(s):
    j = 1
    while i+1 < len(s) and s[i] == s[i+1]:
        j += 1
        i += 1
        continue
    ans.append((j, int(s[i])))
    i += 1
for i in ans:
    print(i, end=" ")
# [(1, '1'), (3, '2'), (1, '3'), (2, '1')]
