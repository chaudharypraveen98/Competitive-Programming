struct Solution{}

impl Solution {
    pub fn hammingWeight (mut n: u32) -> i32 {
        let mut ans = 0;
        while n>0{
            n = n & n-1;
            ans +=1
        }
        return ans
    }
}
fn main() {
    let res = Solution::hammingWeight(678);
    println!("{}",res)
}
