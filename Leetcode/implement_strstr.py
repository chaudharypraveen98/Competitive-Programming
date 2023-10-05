# Constraint first occurrence of needle in haystack=> which implies length of needle must be <= to haystack 
# 0 1 2 3 4       0 1
# h e l l o       l l
 
def strStr2(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    # Finding prefix
    def kmp(str_):
        print(str_)
        b, prefix = 0, [0]
        for i in range(1, len(str_)):
            print(prefix,f"i : {i}, b : {b}",str_[i],str_[b])
            while b > 0 and str_[i] != str_[b]:
                b = prefix[b - 1]
            if str_[b] == str_[i]:
                b += 1
            else:
                b = 0
            prefix.append(b)
        print(prefix)
        return prefix

    str_ = kmp(needle + '#' + haystack)
    n = len(needle)
    if n == 0:
        return n
    for i in range(n + 1, len(str_)):
        if str_[i] == n:
            return i - 2 * n
    return -1

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
  print(strStr2("hello","ll"))