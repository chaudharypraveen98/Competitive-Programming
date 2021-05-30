# Botton up Approach

def num_ways(n,memo):
    memo[1]=1
    memo[2]=2
    for i in range(3,n):
        memo[n] = memo[i-1]+memo[i-2]
    return memo[n]

n = int(input())

# intializing memo table
memo_table = [None for _ in range(n+1)]
print(num_ways(n,memo_table))