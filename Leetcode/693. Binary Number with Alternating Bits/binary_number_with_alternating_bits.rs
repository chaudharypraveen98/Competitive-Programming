struct Solution{}

impl Solution {
    pub fn has_alternating_bits(mut n: i32) -> bool {
        while n!=0 && n>>1!=0{
            let current_bit = n&1;
            if current_bit == (n>>1&1){
                return false;
            }
            n>>=1
        }
        return true;
    }

    pub fn has_alternating_bits1(n: i32) -> bool {
        let temp = (n>>1)+n;
        return (temp&temp+1)==0
    }
}
fn main() {
    let res = Solution::has_alternating_bits(5);
    println!("{}",res);
    let res1 = Solution::has_alternating_bits1(5);
    println!("{}",res1);
}
