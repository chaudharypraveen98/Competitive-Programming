def convert(s,numRows):
  if s is None and numRows <= 0:
      return 0
  if s==1:
      return s

  step = 2*numRows-2
  result=""

  for i in range(0,numRows):
      for j in range(i,len(s),step):
          result+=s[j]
          if i != 0 and i != numRows - 1 and (j + step - 2 * i) < len(s):
              result += s[j + step - 2 * i]
  return result


if __name__ == "__main__":
  a="uqinntq"
  print(convert(a,1))