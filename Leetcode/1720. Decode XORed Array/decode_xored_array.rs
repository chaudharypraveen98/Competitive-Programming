struct Solution{}

impl Solution {
    pub fn decode(encoded: Vec<i32>, first: i32) -> Vec<i32> {
        let mut ans = vec![first];
        for num in encoded{
            ans.push(num^ans.last().unwrap())
        }
        ans
    }
}
fn main() {
    let res = Solution::decode(vec![6,2,7,3],4);
    println!("{:?}",res);
}
