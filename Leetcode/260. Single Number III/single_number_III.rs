struct Solution{}

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let mut xor = 0;
        for num in &nums{
            xor ^=num
        }
        let mask = xor & -xor;
        let mut result1=0;
        let mut result2=0;
        for i in &nums{
            if(i & mask)==0{
                result1 ^=i;
            } else {
                result2 ^=i;
            }
        }
        vec![result1,result2]
    }
}
fn main() {
    let res = Solution::single_number(vec![1,2,1,3,2,5]);
    println!("{:?}",res);
}
