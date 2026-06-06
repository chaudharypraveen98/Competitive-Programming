/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  function dnc(left, right){
    if(left===right){
      return nums[left]
    }
    if(nums[left]<nums[right]){
      return nums[left]
    }
    const mid = Math.floor((left+right)/2)
    return Math.min(dnc(left, mid), dnc(mid+1, right))
  }
  return dnc(0, nums.length-1)
};
console.log(findMin([3, 4, 5, 1, 2]))