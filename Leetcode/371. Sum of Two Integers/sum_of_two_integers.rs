struct Solution{}

impl Solution {
    pub fn get_sum(mut a: i32, mut b: i32) -> i32 {
        while b!=0{
            let carry = (a&b)<<1;
            a = a^b;
            b = carry;
        }
        return a
    }
}
fn main() {
    let res = Solution::get_sum(-12,-90);
    println!("{:?}",res);
}
