## [List Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 97.64%        |

Let's learn about list comprehensions! You are given three integers  *[SVG image]*  and  *[SVG image]*  representing the dimensions of a cuboid along with an integer  *[SVG image]* . Print a list of all possible coordinates given by  *[SVG image]*  on a 3D grid where the sum of  *[SVG image]*  is not equal to  *[SVG image]* . Here,  *[SVG image]* . Please use list comprehensions rather than multiple loops, as a learning exercise. 


**Example**   

 *[SVG image]*    

 *[SVG image]*    

 *[SVG image]*    

 *[SVG image]* 


All permutations of  *[SVG image]*  are:   

 *[SVG image]* . 


Print an array of the elements that do not sum to  *[SVG image]* . 


 *[SVG image]* 

**Input Format**

Four integers  *[SVG image]*  and  *[SVG image]* , each on a separate line. 

**Constraints**

Print the list in lexicographic increasing order.

**Sample Input 0**


```
1
1
1
2

```

**Sample Output 0**


```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

```

**Explanation 0**

Each variable  *[SVG image]*  and  *[SVG image]*  will have values of  *[SVG image]*  or  *[SVG image]* . All permutations of lists in the form  *[SVG image]* .   

Remove all arrays that sum to  *[SVG image]*  to leave only the valid permutations.

**Sample Input 1**


```
2
2
2
2

```

**Sample Output 1**


```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

```


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : List Comprehensions](./list_comprehensions.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/list-comprehensions/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/list-comprehensions/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/list-comprehensions/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/list-comprehensions/editorial) |

