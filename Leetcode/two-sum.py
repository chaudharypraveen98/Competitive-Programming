# only one pair x+y = target we can use that fact
def two_sum(nums,target):
  mem_dict = {}
  for i in range(len(nums)):
    diff = target - nums[i]
    if diff in mem_dict:
      return [mem_dict[diff],i]
    else:
      mem_dict[nums[i]]=i

if __name__ == "__main__":
  nums = [-1,0,1,2,-1,-4]
  print(two_sum(nums,0))