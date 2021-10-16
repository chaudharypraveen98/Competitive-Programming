# A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values
from collections import Counter

# values()
# values are returned in the order first encountered so we dont need ordered dict
d = Counter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
