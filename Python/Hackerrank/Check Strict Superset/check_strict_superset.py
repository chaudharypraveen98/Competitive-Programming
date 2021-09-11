# The all() function returns True if all items in an iterable are true, otherwise it returns False.

super_set = set(input().split())
test_cases = int(input())
res = []
for _ in range(test_cases):
    a = set(input().split())
    res.append(super_set.issuperset(a))
print(all(res))
