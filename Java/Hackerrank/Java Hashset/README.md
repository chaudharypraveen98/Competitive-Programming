## [Java Hashset](https://www.hackerrank.com/challenges/java-hashset)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 96.26%        |

In computer science, a set is an abstract data type that can store certain values, without any particular order, and no repeated values(Wikipedia).  *[SVG image]*  is an example of a set, but  *[SVG image]*  is not a set. Today you will learn how to use sets in java by solving this problem.  



You are given  *[SVG image]*  pairs of strings. Two pairs  *[SVG image]*  and  *[SVG image]*  are identical if  *[SVG image]*  and  *[SVG image]* . That also implies  *[SVG image]*  is *not* same as  *[SVG image]* . After taking each pair as input, you need to print number of unique pairs you currently have.


Complete the code in the editor to solve this problem.

**Input Format**

In the first line, there will be an integer  *[SVG image]*  denoting number of pairs. Each of the next  *[SVG image]*  lines will contain two strings seperated by a single space.


**Constraints:**


* *[SVG image]*
* Length of each string is atmost  *[SVG image]*  and will consist lower case letters only.
**Output Format**

Print  *[SVG image]*  lines. In the  *[SVG image]*  line, print number of unique pairs you have after taking  *[SVG image]*  pair as input.

**Sample Input**


```
5
john tom
john mary
john tom
mary anna
mary anna

```
**Sample Output**


```
1
2
2
3
3

```
**Explanation**

* After taking the first input, you have only one pair: (john,tom)
* After taking the second input, you have two pairs: (john, tom) and (john, mary)
* After taking the third input, you still have two unique pairs.
* After taking the fourth input, you have three unique pairs: (john,tom), (john, mary) and (mary, anna)
* After taking the fifth input, you still have three unique pairs.

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Hashset](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-hashset/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-hashset/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-hashset/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-hashset/editorial) |

