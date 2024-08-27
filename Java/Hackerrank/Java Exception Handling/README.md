## [Java Exception Handling](https://www.hackerrank.com/challenges/java-exception-handling)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 15      | 95.46%        |

You are required to compute the power of a number by implementing a calculator. Create a class *MyCalculator* which consists of a single method `long power(int, int)`. This method takes two integers,  *[SVG image]*  and  *[SVG image]* , as parameters and finds  *[SVG image]* . If either  *[SVG image]*  or  *[SVG image]*  is negative, then the method must throw an exception which says " *[SVG image]* ". Also, if both  *[SVG image]*  and  *[SVG image]*  are zero, then the method must throw an exception which says " *[SVG image]* "


For example, *\-4* and *\-5* would result in  *[SVG image]* .


Complete the function `power` in class *MyCalculator* and return the appropriate result after the power operation or an appropriate exception as detailed above. 

**Input Format**

Each line of the input contains two integers,  *[SVG image]*  and  *[SVG image]* . The locked stub code in the editor reads the input and sends the values to the method as parameters.

**Constraints**

* *[SVG image]*
* *[SVG image]*
**Output Format**

Each line of the output contains the result  *[SVG image]* , if both  *[SVG image]*  and  *[SVG image]*  are positive. If either  *[SVG image]*  or  *[SVG image]*  is negative, the output contains "n and p should be non\-negative". If 
both  *[SVG image]*  and  *[SVG image]*  are zero, the output contains "n and p should not be zero.". This is printed by the locked stub code in the editor.

**Sample Input 0**


```
3 5
2 4
0 0
-1 -2
-1 3

```

**Sample Output 0**


```
243
16
java.lang.Exception: n and p should not be zero.
java.lang.Exception: n or p should not be negative.
java.lang.Exception: n or p should not be negative.

```

**Explanation 0**

* In the first two cases, both  *[SVG image]*  and  *[SVG image]*  are postive. So, the power function returns the answer correctly.
* In the third case, both  *[SVG image]*  and  *[SVG image]*  are zero. So, the exception, "n and p should not be zero.", is printed.
* In the last two cases, at least one out of  *[SVG image]*  and  *[SVG image]*  is negative. So, the exception, "n or p should not be negative.", is printed for these two cases.

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Exception Handling](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-exception-handling/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-exception-handling/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-exception-handling/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-exception-handling/editorial) |

