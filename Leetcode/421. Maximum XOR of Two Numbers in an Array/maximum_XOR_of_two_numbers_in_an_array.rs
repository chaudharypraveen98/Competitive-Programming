use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn find_maximum_xor(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in (0..32).rev() {
            ans <<= 1;
            let prefixes: HashSet<i32> = nums.iter().map(|&num| num >> i).collect();
            ans += prefixes.iter().any(|&a| prefixes.contains(&(ans ^ 1 ^ a))) as i32;
        }
        ans
    }
}

fn main() {
    let sol = Solution::find_maximum_xor(vec![14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]);
    println!("{:?}", sol);
}