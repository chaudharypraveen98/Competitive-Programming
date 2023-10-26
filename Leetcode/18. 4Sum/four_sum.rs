struct Solution {}

impl Solution {
    pub fn four_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>>{
        let mut res: Vec<Vec<i32>> = Vec::new();
        if nums.len()<4{
            return res;
        }
        let mut nums = nums;
        nums.sort();
        println!("{:?}",nums);
        for i in 0..nums.len()-3{
            if i>0 && nums[i]==nums[i-1]{
                continue;
            }
            for j in i+1..nums.len()-2{
                if j>i+1 && nums[j]==nums[j-1] {
                    continue;
                }
                let mut left = j+1;
                let mut right = nums.len()-1;
                while left<right{
                    let four_sum = nums[i] as i64+nums[j] as i64+nums[left]as i64+nums[right] as i64;
                    if four_sum==target as i64{
                        res.push(vec![nums[i],nums[j],nums[left],nums[right]]);
                        while left<right && nums[left]==nums[left+1]{
                            left+=1;
                        }
                        while left<right && nums[right]==nums[right-1]{
                            right-=1;
                        }
                        left+=1;
                        right-=1;
                    } else if four_sum>target as i64 {
                        right-=1;
                    } else{
                        left+=1;
                    }
                }

            }
        }
        res
    }
}
fn main() {
    let res = Solution::four_sum(vec![1000000000,1000000000,1000000000,1000000000],-294967296);
    println!("{:?}", res);
}
