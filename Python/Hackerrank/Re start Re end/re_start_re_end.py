import re

S = input()
k = input()

# it will search all the k pattern in s
m = re.search(k, S)

# the main advantage for using compiled regex if your re-using the same regex multiple times,
# thereby reducing the possibility for typos.
# If your just calling it once then uncompiled is more readable
pattern = re.compile(k)
if not m: print("(-1, -1)")
while m:
    print(f"({m.start()}, {m.end() - 1})")
    m = pattern.search(S, m.start() + 1)
