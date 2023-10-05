# Base condition: [] => ""
# only one item ["text"] => "text"


def longestCommonPrefix(strs):
  if len(strs)==0:
    return ""
  res=strs[0]
  for i in strs[1:]:
    min_of_both = min(len(res),len(i))
    res=res[:min_of_both]
    for j in range(min_of_both):
      if i[j]!=res[j]:
        res= i[:j]
        break
  return res

if __name__ == "__main__":
  a= ["flower","flow","florwht"]
  print(longestCommonPrefix(a))