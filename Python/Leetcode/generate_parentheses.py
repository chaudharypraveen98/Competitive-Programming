def generate_parenthesis(a):
  # print(generate("",a,a))
  return generator("",a,a)

# This approach is called backtracking
def generate(p, left, right, parens=[]):
  # We are using Mutable Default Arguments parens https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
  if left:         generate(p + '(', left-1, right)
  if right > left: generate(p + ')', left, right-1)

  # it ensures that the limit of pattern an collecting result
  if not right:    parens += p,
  return parens

def generator(prefix,l_brac,r_brac,res=[]): 
  if l_brac==0 and r_brac==0:
    res.append(prefix)
  if r_brac>=0:
    # last character must be ")"
    if l_brac==0 and r_brac==1:
      generator(prefix+")",l_brac,r_brac-1)
    elif prefix:
      if l_brac:
        generator(prefix+"(",l_brac-1,r_brac)
      if r_brac>l_brac:
        generator(prefix+")",l_brac,r_brac-1)
    else:
      # first character must be "("
      generator(prefix+"(",l_brac-1,r_brac)
  return res

if __name__ == "__main__":
  a=3
  print(generate_parenthesis(a))