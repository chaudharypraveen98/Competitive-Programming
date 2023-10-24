use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut nums_map: HashMap<i32, usize> = HashMap::with_capacity(nums.len());
        for (i, &num) in nums.iter().enumerate() {
            let second_no = target - num;
            if let Some(&index) = nums_map.get(&second_no) {
                return vec![index as i32, i as i32];
            }
            nums_map.insert(num, i);
        }
        unreachable![]
    }
}
fn main() {
    let res = Solution::two_sum(vec![3, 2, 4], 6);
    println!("{:?}", res);
}
