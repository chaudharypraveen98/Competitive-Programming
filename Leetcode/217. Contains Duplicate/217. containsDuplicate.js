/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let hashmap = new Set();
    for(let i = 0; i< nums.length; i++){
        if(hashmap.has(nums[i])){
            return true
        } else {
            hashmap.add(nums[i])
        }
    }
    return false
};

console.log(containsDuplicate([1,2,3,4, 3, 5]))