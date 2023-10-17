use std::collections::{HashSet, HashMap};

struct Solution{}

impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        let mut cur:u32 = 0;
        let n2d:HashMap<char,u32> =[('A', 0), ('C', 1), ('G', 3), ('T', 2)].iter().cloned().collect();
        let mut candidates:HashSet<u32> = HashSet::new();
        let mut duplicates:HashSet<String> = HashSet::new();
        for (ch,i) in s.chars().zip(0..){
            cur &=((1 as u32)<<18)-1;
            cur = cur * 4 + n2d[&ch];
            if i >= 9 {
                if candidates.contains(&cur) {
                    duplicates.insert(s.chars().skip(i as usize - 9).take(10).collect());
                } else {
                    candidates.insert(cur);
                }
            }
        }
        duplicates.into_iter().collect()
    }
}
fn main() {
    let res = Solution::find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT".to_string());
    println!("{:?}",res);
}
