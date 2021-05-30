test_str = input()

def decode(message,k,memo):
    if k==0:
        return 1
    
    # checking memo table if its already there
    if memo[k]:
        return memo[k]
    s = len(message)-k
    
    if message[s]=="0":
        return 0
    
    # taking single character
    result = decode(message,k-1,memo)
    
    # taking two character and checking if its valid
    if k>1 and int(message[s:s+2])<27:
        result+= decode(message,k-2,memo)

    # storing for further use
    memo[k]=result
    return result

# memo table to save intermediate result    
memo_table = [None for i in range(len(test_str)+1)]
print(decode(test_str,len(test_str),memo_table))