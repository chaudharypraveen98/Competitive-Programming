# Constraint first occurrence of needle in haystack=> which implies length of needle must be <= to haystack 
# 0 1 2 3 4       0 1
# h e l l o       l l

def strStr(haystack,needle):
  if not needle:
    return 0
  for index,i in enumerate(haystack):
    if len(needle)>len(haystack)-index:
      return -1
    if i==needle[0]:
      if haystack[index:index+len(needle)]==needle:
        return index
  return -1

if __name__ == "__main__":
  print(strStr("hello","ll"))