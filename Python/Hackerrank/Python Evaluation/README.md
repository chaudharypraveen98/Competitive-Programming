## [Python Evaluation](https://www.hackerrank.com/challenges/python-eval)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 20      | 96.38%        |

The `eval()` expression is a very powerful built\-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object. 


For example: 



```
>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5

```

Here, `eval()` can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings. 


For example:



```
>>> type(eval("len"))
<type 'builtin_function_or_method'>

```

Without eval()



```
>>> type("len")
<type 'str'>

```

**Task**   

You are given an expression in a line. Read that line as a string variable, such as *var*, and print the result using *eval(var)*. 


**NOTE**: Python2 users, please import `from __future__ import print_function`. 


**Constraint**   

Input string is less than 100 characters. 


**Sample Input** 



```
print(2 + 3)

```

**Sample Output** 



```
5

```


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Python Evaluation](./python_evaluation.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/python-eval/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/python-eval/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/python-eval/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/python-eval/editorial) |

