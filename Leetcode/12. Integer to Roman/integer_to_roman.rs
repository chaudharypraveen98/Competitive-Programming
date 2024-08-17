struct Solution {}

impl Solution {
    pub fn int_to_roman(mut num: i32) -> String {
        let values = vec![ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ];
        let numerals = vec![ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ];
        let mut res = String::new();
        for i in 0..values.len() {
            let q = (num/values[i]) as usize;
            if q!=0 {
                num = num%values[i];
                res.push_str(&numerals[i].repeat(q))
            }
        }
        res
    }
}
fn main() {
    let res = Solution::int_to_roman(3749);
    println!("{:?}", res);
    // res -> MMMDCCXLIX
}
