def lengthOfLongestSubstring(s):
  max_len = 0
  for index,i in enumerate(s):
    unique_elements=set(i)
    temp_length = 1
    for j in s[index+1:]:
      if j not in unique_elements:
        temp_length+=1
        unique_elements.add(j)
      else:
        break
    if(temp_length>max_len):
      max_len=temp_length
  return max_len

def lengthOfLongestSubstring1(s):
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)  
        used[c] = i
    return max_length

if __name__ == "__main__":
  a="uqinntq"
  print(lengthOfLongestSubstring1(a))