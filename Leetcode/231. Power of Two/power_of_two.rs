struct Solution{}

impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        let bitwise_and = (n & n-1)==0;
        bitwise_and && n!=0
    }
}
fn main() {
    let res = Solution::is_power_of_two(-2147483648);
    println!("{}",res);
}
