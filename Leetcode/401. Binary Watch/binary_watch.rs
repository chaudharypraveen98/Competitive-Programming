struct Solution{}

impl Solution {
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        let mut result = Vec::new();
        let nu = turned_on as u32;
        for h in 0i32..12{
            for m in 0i32..60{
                if (h.count_ones() + m.count_ones()) == nu {
                    result.push(format!("{}:{:02}", h, m));
                }
            }
        }
        result
    }
}
fn main() {
    let res = Solution::read_binary_watch(2);
    println!("{:?}",res);
}
