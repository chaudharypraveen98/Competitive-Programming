struct Solution{}

impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut ans = vec![];
        for mut i in 0..n+1{
            let mut count =0;
            while i>0{
                i &=i-1;
                count+=1
            }
            ans.push(count)
        }
        ans
    }
}
fn main() {
    let res = Solution::count_bits(5);
    println!("{:?}",res)
}
