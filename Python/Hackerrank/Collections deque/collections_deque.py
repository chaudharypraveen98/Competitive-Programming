from collections import deque

# getattr takes a object( here deque ) as a first parameter and atrribute name as a second Arguement
# Deque is like a queue but has both end to exit

d = deque()
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(d, cmd)(*args)
[print(x, end=' ') for x in d]
