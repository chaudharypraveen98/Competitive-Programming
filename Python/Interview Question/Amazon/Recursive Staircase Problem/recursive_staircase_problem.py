# Recursive Approach
## The problem is that itt will give maximum recursion depth exceeded error
def num_ways(n):
    if n==1:
        return 1
    if n==2:
        return 2
    result  = num_ways(n-1)
    if n>1:
        result+= num_ways(n-2)
    return result

n = int(input())
print(num_ways(n))