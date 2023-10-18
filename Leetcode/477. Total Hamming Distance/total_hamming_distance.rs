use std::collections::{HashSet, HashMap};

struct Solution{}

impl Solution {
    pub fn total_hamming_distance(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        for i in 0..32{
            let mut count = 0;
            for num in &nums{
                count += (num>>i)&1;
            }
            res += count * (nums.len() as i32 -count)
        }
        res
    }
}
fn main() {
    let res = Solution::total_hamming_distance(vec![4,14,2]);
    println!("{:?}",res);
}
