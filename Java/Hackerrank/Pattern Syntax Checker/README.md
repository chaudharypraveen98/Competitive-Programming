## [Pattern Syntax Checker](https://www.hackerrank.com/challenges/pattern-syntax-checker)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 20      | 97.50%        |

Using **Regex**, we can easily match or search for patterns in a text. Before searching for a pattern, we have to specify one using some well\-defined syntax.


In this problem, you are given a pattern. You have to check whether the syntax of the given pattern is valid.


**Note**: In this problem, a regex is only valid if you can compile it using the [Pattern.compile](http://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html#compile%28java.lang.String%29) method.

**Input Format**

The first line of input contains an integer  *[SVG image]* , denoting the number of test cases. The next  *[SVG image]*  lines contain a string of any printable characters representing the pattern of a regex.

**Output Format**

For each test case, print `Valid` if the syntax of the given pattern is correct. Otherwise, print `Invalid`. Do not print the quotes.

**Sample Input**


```
3
([A-Z])(.+)
[AZ[a-z](a-z)
batcatpat(nat

```
**Sample Output**


```
Valid
Invalid
Invalid

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Pattern Syntax Checker](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/pattern-syntax-checker/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/pattern-syntax-checker/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/pattern-syntax-checker/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/pattern-syntax-checker/editorial) |

