struct Solution {}

impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut sorted_array = heights.clone();
        sorted_array.sort();
        let mut answer = 0;
        for num in 0..heights.len(){
            if heights[num] != sorted_array[num]{
                answer+=1;
            }
        }
        answer
    }
}

fn main() {
    let res = Solution::height_checker(vec![5,1,2,3,4]);
    println!("{:?}", res);
}
