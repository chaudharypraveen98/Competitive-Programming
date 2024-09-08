## [Piling Up!](https://www.hackerrank.com/challenges/piling-up)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Medium       | 50      | 90.88%        |

There is a horizontal row of  *[SVG image]*  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  *[SVG image]*  is on top of  *[SVG image]*  then  *[SVG image]* . 


When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print `Yes` if it is possible to stack the cubes. Otherwise, print `No`. 


**Example**   

 *[SVG image]*  


Result: `No` 


After choosing the rightmost element,  *[SVG image]* , choose the leftmost element,  *[SVG image]* . After than, the choices are  *[SVG image]*  and  *[SVG image]* . These are both larger than the top block of size  *[SVG image]* .


 *[SVG image]*  


Result: `Yes`


Choose blocks from right to left in order to successfully stack the blocks. 

**Input Format**

The first line contains a single integer  *[SVG image]* , the number of test cases.   

For each test case, there are  *[SVG image]*  lines.   

The first line of each test case contains  *[SVG image]* , the number of cubes.   

The second line contains  *[SVG image]*  space separated integers, denoting the *sideLengths* of each cube in that order. 

**Constraints**

 *[SVG image]*    

 *[SVG image]*    

 *[SVG image]* 

**Output Format**

For each test case, output a single line containing either `Yes` or `No`.

**Sample Input**


```
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]

```
**Sample Output**


```
Yes
No

```
**Explanation**

In the first test case, pick in this order: **left \-  *[SVG image]* , right \-  *[SVG image]* , left \-  *[SVG image]* , right \-  *[SVG image]* , left \-  *[SVG image]* , right \-  *[SVG image]*** .   

 In the second test case, no order gives an appropriate arrangement of vertical cubes.  *[SVG image]*  will always come after either  *[SVG image]*  or  *[SVG image]* .


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Piling Up!](./piling_up.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/piling-up/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/piling-up/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/piling-up/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/piling-up/editorial) |

