# Recursive Approach with memo

def num_ways(n,memo):

    # checking memo table
    if memo[n]:
        return n
    if n==1:
        return 1
    if n==2:
        return 2
    result  = num_ways(n-1,memo)
    if n>1:
        result+= num_ways(n-2,memo)
    
    # saving intermediate result
    memo[n]=result
    return result

n = int(input())

# intializing memo table
memo_table = [None for _ in range(n+1)]
print(num_ways(n,memo_table))