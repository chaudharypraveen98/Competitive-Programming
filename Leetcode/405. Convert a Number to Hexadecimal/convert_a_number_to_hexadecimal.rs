struct Solution{}

impl Solution {
    pub fn to_hex(num: i32) -> String {
        let mut num = num as u32;
        if num==0{
            return '0'.to_string()
        }
        let hex_str  =["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"];
        let mut hex_code ="".to_string();
        while num>0{
            let digit = num%16;
            hex_code.insert_str(0,hex_str[digit as usize]);
            num>>=4;
        }
        hex_code
    }
}
fn main() {
    let res = Solution::to_hex(26);
    println!("{}",res);
}
