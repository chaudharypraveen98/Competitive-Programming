struct Solution{}

impl Solution {
    pub fn range_bitwise_and(mut left: i32, mut right: i32) -> i32 {
        let mut count =0;
        while left !=right{
            left>>=1;
            right>>=1;
            count+=1
        }
        left<<count
        
    }
}
fn main() {
    let res = Solution::range_bitwise_and(5,7);
    println!("{}",res)
}
