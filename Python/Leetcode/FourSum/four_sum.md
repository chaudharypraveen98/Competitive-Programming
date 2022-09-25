## Steps:
1. Take `i` for loop from 0 to length (no of elements left -1)
2. Check for repetion for i using `nums[i]==nums[i-1]`
3. Take **left**, **mid** and **right**.
4. Check for repetion with the help of **left**
5. loop while **mid < right**
6. get **sum**
   1. if sum > target: **right-=1**
   2. if sum < target: **mid+=1**
   3. else:
      1. append to result
      2. reposition the **mid** and checking for repition : mid+=1
      3. reposition the **mid** and checking for repition : right-=1
      4. mid+=1
      5. right-=1