## [Java 2D Array](https://www.hackerrank.com/challenges/java-2d-array)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 92.96%        |

You are given a  *[SVG image]*  2D array. An hourglass in an array is a portion shaped like this:



```
a b c
  d
e f g

```

For example, if we create an hourglass using the number 1 within an array full of zeros, it may look like this:



```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

```

Actually, there are many hourglasses in the array above. The three leftmost hourglasses are the following:



```
1 1 1     1 1 0     1 0 0
  1         0         0
1 1 1     1 1 0     1 0 0

```

The sum of an hourglass is the sum of all the numbers within it. The sum for the hourglasses above are 7, 4, and 2, respectively.


In this problem you have to *print the largest sum among all the hourglasses* in the array.

**Input Format**

There will be exactly  *[SVG image]*  lines, each containing  *[SVG image]*  integers seperated by spaces. Each integer will be between  *[SVG image]*  and  *[SVG image]*  inclusive.

**Output Format**

Print the answer to this problem on a single line.

**Sample Input**


```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

```
**Sample Output**


```
19

```
**Explanation**

The hourglass which has the largest sum is:



```
2 4 4
  2
1 2 4

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java 2D Array](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-2d-array/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-2d-array/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-2d-array/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-2d-array/editorial) |

