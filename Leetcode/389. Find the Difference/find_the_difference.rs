struct Solution{}

impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut ans =0;
        for i in s.chars(){
            ans ^= i as u8;
        }
        for j in t.chars(){
            ans ^= j as u8;
        }
        return char::from(ans)
    }
    pub fn find_the_difference1(s: String, t: String) -> char {
        let mut s_sum=0;
        let mut t_sum=0;
        for i in s.chars(){
            s_sum += i as u16;
        }
        for j in t.chars(){
            t_sum += j as u16;
        }
        return char::from((t_sum-s_sum) as u8)
    }
}
fn main() {
    let res = Solution::find_the_difference(String::from("abcd"),String::from("abcde"));
    println!("{}",res);
    let res1 = Solution::find_the_difference1(String::from("abcd"),String::from("abcde"));
    println!("{}",res1)
}
