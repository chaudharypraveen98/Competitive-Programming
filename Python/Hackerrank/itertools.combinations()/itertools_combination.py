from itertools import combinations
# combination function from iter tools makes all the possible combinations possible

word, length = input().split()
for i in range(1, int(length) + 1):
    for j in list(combinations(sorted(word), i)):
        # join the list separated with no space
        print("".join(j))
