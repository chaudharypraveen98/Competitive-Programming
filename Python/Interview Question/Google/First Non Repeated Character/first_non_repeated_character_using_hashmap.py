test_str = input()
hashmap = {}
for index,character in enumerate(test_str):
    if character not in hashmap:
        hashmap[character] = [1,index]
    else:
        hashmap[character][0] +=1
result =("",len(test_str))
for key,value in hashmap.items():
    if value[0]==1 and value[1]<result[1]:
        result = (key,value[1])
print(result[0])