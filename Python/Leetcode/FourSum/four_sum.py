# finding three sum 
# Time complexity O(N^2)
from operator import le


def sub_three_sum(nums, target,starting_point):
    result = []
    for left in range(starting_point+1,len(nums)-2):
        # checking duplicates in first loop
        if left>starting_point+1 and nums[left]==nums[left-1]:
            continue
        mid = left + 1
        right = len(nums)-1
        while mid<right:
            sum_of_all = nums[starting_point]+nums[left]+nums[mid]+nums[right]
            if sum_of_all>target:
                right -= 1
            elif sum_of_all <target:
                mid +=1
            else:
                result.append([nums[starting_point],nums[left],nums[mid],nums[right]])

                # two while loops are for checking duplicates in a particular iteration
                while mid<right and nums[mid]==nums[mid+1]:
                    mid +=1
                while mid<right and nums[right]==nums[right-1]:
                    right -=1
                mid +=1
                right -=1
    return result

# Time complexity O(N)
def four_sum(nums, target):
    nums.sort()
    result=[]
    for i in range(len(nums)-3):
      #checking duplicates
        if i>0 and nums[i]==nums[i-1]:
            continue
        result.extend(sub_three_sum(nums,target,i))
    return result

if __name__ == "__main__":
  nums = [2,2,2,2]
  print(four_sum(nums,8))