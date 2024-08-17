struct Solution {}

impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n<2{
            return n
        }
        return Self::fib(n-1)+Self::fib(n-2)
    }
    pub fn fib1(n: i32) -> i32 {
        if n<2{
            return n;
        }
        let mut values = vec![0,1];
        for i in 2..n+1 {
            values.push(values[i as usize-1]+values[i as usize -2])
        }
        return values[n as usize]
    }
}
fn main() {
    let res = Solution::fib(5);
    println!("{:?}", res);
    let res1 = Solution::fib1(5);
    println!("{:?}", res1);
    // res -> 5
}
