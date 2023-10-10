struct Solution{}

impl Solution {
    pub fn find_complement(num: i32) -> i32 {
        let mut total_bits = 0;
        let mut n = num;
        while n!=0{
            n>>=1;
            total_bits+=1
        }
        let mask = (1<<total_bits)-1;
        return num ^ mask
    }
}
fn main() {
    let res = Solution::find_complement(5);
    println!("{}",res);
}
