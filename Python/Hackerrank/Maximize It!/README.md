## [Maximize It!](https://www.hackerrank.com/challenges/maximize-it)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Hard       |    50     |        81.86% |

You are given a function f(X)=X^2 . You are also given `K `lists. The `i'th` list consists of `N`i elements.
You have to pick one element from each list so that the value from the equation below is maximized:  
`S=(f(X1)+f(X2)+f()+....f(Xk))% M`

`X`i denotes the element picked from the list . Find the maximized value obtained.  
`%` denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.  

**Input Format**

The first line contains  *[SVG image]*  space separated integers  *[SVG image]*  and  *[SVG image]* .   

The next  *[SVG image]*  lines each contains an integer  *[SVG image]* , denoting the number of elements in the  *[SVG image]*  list, followed by  *[SVG image]*  space separated integers denoting the elements in the list. 

**Constraints**

 *[SVG image]*    

 *[SVG image]*    

 *[SVG image]*    

 *[SVG image]*  

**Output Format**

Output a single integer denoting the value  *[SVG image]* . 

**Sample Input**


```
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

```
**Sample Output**


```
206

```
**Explanation**
Picking `5` from the `1`st list, `9` from the `2`nd list and `10` from the `3`rd list gives the maximum  `S` value equal to (`5`^2 + `9`^2 + `10`^2) % `1000`= 206.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Maximize It!](./maximize_it.py)

| Submissions                                                                      |                                      Leaderboard                                      |                                                                      Discussions |                                                                  Editorial |
| :------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------------: | -------------------------------------------------------------------------------: | -------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/maximize-it/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/maximize-it/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/maximize-it/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/maximize-it/editorial) |

