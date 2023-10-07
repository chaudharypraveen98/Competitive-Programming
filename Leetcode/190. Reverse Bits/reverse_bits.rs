struct Solution{}

impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut ans =0;
        for i in 0..32u32{
            let last_bit = x>>i&1;
            ans = ans |(last_bit<<(31-i))
        }
        ans
        
    }
}
fn main() {
    let res = Solution::reverse_bits(43261596);
    println!("{}",res)
}
