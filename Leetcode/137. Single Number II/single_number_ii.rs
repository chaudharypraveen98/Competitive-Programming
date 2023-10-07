struct Solution{}

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..32{
            let mut bit_sum = 0;
            for num in &nums{
                bit_sum = bit_sum + (num>>i & 1)
            }
            bit_sum = bit_sum % 3;
            ans = ans | (bit_sum<<i)
        }
        ans
        
    }
}
fn main() {
    let res = Solution::single_number(vec![0,1,0,1,0,1,99]);
    println!("{}",res)
}
