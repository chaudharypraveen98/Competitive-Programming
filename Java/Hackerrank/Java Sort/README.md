## [Java Sort](https://www.hackerrank.com/challenges/java-sort)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 94.82%        |

You are given a list of student information: ID, FirstName, and CGPA. Your task is to rearrange them according to their CGPA in decreasing order. If two student have the same CGPA, then arrange them according to their first name in alphabetical order. If those two students also have the same first name, then order them according to their ID. No two students have the same ID.


**Hint**: You can use comparators to sort a list of objects. See the [oracle docs](http://docs.oracle.com/javase/tutorial/collections/interfaces/order.html) to learn about comparators.

**Input Format**

The first line of input contains an integer  *[SVG image]* , representing the total number of students. The next  *[SVG image]*  lines contains a list of student information in the following structure:



```
ID Name CGPA

```

**Constraints**


 *[SVG image]*   

 *[SVG image]*   

 *[SVG image]*   

 *[SVG image]*   



The name contains only lowercase English letters. The  *[SVG image]*  contains only integer numbers without leading zeros. The *CGPA* will contain, at most, 2 digits after the decimal point.

**Output Format**

After rearranging the students according to the above rules, print the first name of each student on a separate line.

**Sample Input**


```
5
33 Rumpa 3.68
85 Ashis 3.85
56 Samiha 3.75
19 Samara 3.75
22 Fahim 3.76

```
**Sample Output**


```
Ashis
Fahim
Samara
Samiha
Rumpa

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Sort](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-sort/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-sort/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-sort/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-sort/editorial) |

