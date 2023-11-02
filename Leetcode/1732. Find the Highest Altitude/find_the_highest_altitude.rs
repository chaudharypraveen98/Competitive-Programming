struct Solution {}

impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut largest = 0;
        let mut sum_all = 0;
        for current_gain in gain{
            sum_all+=current_gain;
            if sum_all>largest{
                largest = sum_all;
            }
        }
        largest
    }
}

fn main() {
    let res = Solution::largest_altitude(vec![-4,-3,-2,-1,4,3,2]);
    println!("{:?}", res);
}
