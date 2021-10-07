test_cases = int(input())
for i in range(test_cases):
    length_a = input()
    set_a = set(input().split())
    length_b = input()
    set_b = set(input().split())
    print(set_a.issubset(set_b))
