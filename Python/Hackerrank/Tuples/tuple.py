n = int(input())

# map will convert the input string to int
integer_list = map(int, input().split())

# just using the hash function
print(hash(tuple(integer_list)))