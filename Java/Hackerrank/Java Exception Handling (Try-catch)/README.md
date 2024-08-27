## [Java Exception Handling (Try-catch)](https://www.hackerrank.com/challenges/java-exception-handling-try-catch)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 94.70%        |

Exception handling is the process of responding to the occurrence, during computation, of exceptions – anomalous or exceptional conditions requiring special processing – often changing the normal flow of program execution. (Wikipedia)




---


Java has built\-in mechanism to handle exceptions. Using the *try* statement we can test a block of code for errors. The *catch* block contains the code that says what to do if exception occurs. 


This problem will test your knowledge on try\-catch block.


You will be given two integers  *[SVG image]*  and  *[SVG image]*  as input, you have to compute  *[SVG image]* . If  *[SVG image]*  and  *[SVG image]*  are not  *[SVG image]*  bit signed integers or if  *[SVG image]*  is zero, exception will occur and you have to report it. Read sample Input/Output to know what to report in case of exceptions.


**Sample Input 0:**



```
10
3

```

**Sample Output 0:**



```
3

```

**Sample Input 1:**



```
10
Hello

```

**Sample Output 1:**



```
java.util.InputMismatchException

```

**Sample Input 2:**



```
10
0

```

**Sample Output 2:**



```
java.lang.ArithmeticException: / by zero

```

**Sample Input 3:**



```
23.323
0

```

**Sample Output 3:**



```
java.util.InputMismatchException

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Exception Handling (Try-catch)](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-exception-handling-try-catch/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-exception-handling-try-catch/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-exception-handling-try-catch/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-exception-handling-try-catch/editorial) |

