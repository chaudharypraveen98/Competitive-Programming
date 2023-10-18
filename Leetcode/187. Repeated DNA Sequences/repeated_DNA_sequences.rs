use std::collections::{HashSet, HashMap};

struct Solution{}

impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        if s.len()<10{
            return vec![];
        }
        let mut sequence:HashSet<&str> = HashSet::new();
        let mut duplicates:HashSet<&str> = HashSet::new();
        for i in 0..s.len()-9{
            let curr_pattern = &s[i..i+10];
            if sequence.contains(curr_pattern){
                duplicates.insert(curr_pattern);
            } else {
                sequence.insert(curr_pattern);
            }
        }
        duplicates.into_iter().map(String::from).collect()
    }
    pub fn find_repeated_dna_sequences1(s: String) -> Vec<String> {
        if s.len()<10{
            return vec![];
        }
        let n2d:HashMap<char,u32> =[('A', 0), ('C', 1), ('G', 3), ('T', 2)].iter().cloned().collect();
        let mut count_map:HashMap<i32, i32> = HashMap::new();
        let mut encoded_input:Vec<i32> = Vec::new();
        for i in s.chars(){
            encoded_input.push(n2d[&i] as i32)
        }
        let mut cur_hash = 0;
        let mut res:Vec<String> = Vec::new();
        let base:i32 = 4;
        for i in 0..10{
            cur_hash = cur_hash * base + encoded_input[i];
        }
        count_map.insert(cur_hash.clone(), 1);
        for i in 1..(s.len()-9){
            cur_hash = cur_hash*base - encoded_input[i-1]*(base.pow(10))+encoded_input[i+9];
            if count_map.contains_key(&cur_hash) {
                count_map.insert(cur_hash.clone(), count_map.get(&cur_hash).unwrap()+1);
                if count_map.get(&cur_hash).unwrap().clone()== 2_i32{
                    res.push(s.chars().skip(i).take(10).collect())
                }
                
            } else {
                count_map.insert(cur_hash.clone(), 1);
            }
        }
        res
    }
    pub fn find_repeated_dna_sequences2(s: String) -> Vec<String> {
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
    let res1 = Solution::find_repeated_dna_sequences1("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT".to_string());
    let res2= Solution::find_repeated_dna_sequences2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT".to_string());
    println!("{:?}\n{:?}\n{:?}",res,res1,res2);
}
