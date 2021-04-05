# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# input().split() takes input continously separated by "-", " "
# m => size of group A, n => size of group B
m,n = map(int,input().split())

#intializing the defaultDict
d = defaultdict(list)

for i in range(m):
    group_m = input()

    # str(i+1) stores the index of the item
    d[group_m].append(str(i+1))

for i in range(n):
    group_n = input()

    # It will check the key if its empty or not
    if d[group_n]:
        print(" ".join(d[group_n]))
    else:
        print("-1")