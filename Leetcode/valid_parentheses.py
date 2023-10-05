def is_valid(s):
    hashmap = {"(":")","[":"]","{":"}"}
    stack=[]
    for bracket in s:
        if bracket in hashmap:
            stack.append(hashmap[bracket])
        else:
            if not stack or bracket!=stack.pop():
                return False
    return stack==[]

if __name__ == "__main__":
  s = "(){}"
  print(is_valid(s))