struct Solution{}

impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
        if n==0{
            return false;
        }
        let mask = 0b01010101010101010101010101010101;
        let one_set_bit = n&n-1==0;
        if one_set_bit{
            return mask == mask|n
        }
        false
    }
}
fn main() {
    let res = Solution::is_power_of_four(16);
    println!("{}",res);
}
