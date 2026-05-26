/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  let maxProduct = nums[0];
  let res = nums[0];
  let minProduct = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] < 0) {
      [maxProduct, minProduct] = [minProduct, maxProduct];
    }
    maxProduct = Math.max(nums[i], nums[i] * maxProduct);
    minProduct = Math.min(nums[i], nums[i] * minProduct);
    res = Math.max(res, maxProduct);
  }
  return res === -0 ? 0 : res;
};

// Kadane Algorithms

var maxProduct1 = function (nums) {
  let prefix = 0;
  let suffix = 0;
  let res = nums[0];
  let n = nums.length;
  
  for (let i = 0; i < n; i++) {
    // If prefix or suffix hit 0 due to previous element, reset to 1
    prefix = (prefix === 0 ? 1 : prefix) * nums[i];
    suffix = (suffix === 0 ? 1 : suffix) * nums[n - 1 - i];
    
    res = Math.max(res, prefix, suffix);
  }
  
  // Hardened check against Signed Zero (-0)
  return res === -0 ? 0 : res;
};
