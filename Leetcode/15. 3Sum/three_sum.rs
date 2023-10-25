struct Solution {}

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut nums = nums;
        nums.sort();
        for i in 0..nums.len() - 2 {
            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }
            let mut left = i+1;
            let mut right = nums.len() - 1;
            while left < right {
                let sum_three = nums[i] + nums[left] + nums[right];
                if sum_three == 0 {
                    res.push(vec![nums[i], nums[left], nums[right]]);
                    while left < right && nums[left] == nums[left + 1] {
                        left += 1;
                    }
                    while left < right && nums[right] == nums[right - 1] {
                        right -= 1;
                    }
                    left += 1;
                    right -= 1;
                } else if sum_three > 0 {
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }
        res
    }
}
fn main() {
    let res = Solution::three_sum(vec![1,2,-2,-1]);
    println!("{:?}", res);
}
