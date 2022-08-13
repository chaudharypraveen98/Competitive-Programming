def compute_lps(pattern,M,lps):
  lps[0]=0
  i=1
  # length of matching prefix which is also suffix
  # i and len_p_s are the two pointers on the same pattern
  len_p_s = 0
  while i<M:
    if pattern[i]==pattern[len_p_s]:
      lps[i]= len_p_s+1
      len_p_s+=1
      i+=1
    else:
      if len_p_s!=0:
        len_p_s = lps[len_p_s-1]
      else:
        lps[i]=0
        i+=1
  return lps

def kmp(text,pattern):
  """
  :type text: str
  :type pattern: str
  :rtype: int
  """
  N = len(text)
  M = len(pattern)
  lps = [0]*M
  i=0
  j=0
  compute_lps(pattern,M,lps)
  print(lps)
  while i<N:
    if text[i]==pattern[j]:
      i+=1
      j+=1
    else:
      if j!=0:
        j = lps[j-1]
      else:
        i+=1
    if j==M:
      return i-j
      # for finding repeated pattern 
      # j = lps[j-1]


if __name__ == "__main__":
  print(kmp("AAAABAAAAABBBAAAAB","AAAB"))