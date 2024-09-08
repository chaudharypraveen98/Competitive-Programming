## [Exceptions](https://www.hackerrank.com/challenges/exceptions)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    10     |        96.04% |

### [Exceptions](https://docs.python.org/2/tutorial/errors.html#exceptions)


Errors detected during execution are called *exceptions*.


**Examples**:


[***ZeroDivisionError***](https://docs.python.org/2/library/exceptions.html#exceptions.ZeroDivisionError)   

This error is raised when the second argument of a division or modulo operation is zero.



```
>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero

```

[***ValueError***](https://docs.python.org/2/library/exceptions.html#exceptions.ValueError)   

This error is raised when a built\-in operation or function receives an argument that has the right type but an inappropriate value. 



```
>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'

```

 To learn more about different built\-in exceptions **[click here](https://docs.python.org/2/library/exceptions.html#module-exceptions)**. 


### [Handling Exceptions](https://docs.python.org/2/tutorial/errors.html#handling-exceptions)


The statements *try* and *except* can be used to handle selected exceptions. A *try* statement may have more than one except clause to specify handlers for different exceptions.



```
#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e

```

**Output**


Error Code: integer division or modulo by zero




---


**Task**


You are given two values *a* and *b*.
Perform integer division and print *a/b*.

**Input Format**

The first line contains  *[SVG image]* , the number of test cases.   

The next  *[SVG image]*  lines each contain the space separated values of  *[SVG image]*  and  *[SVG image]* .


**Constraints**


* *[SVG image]*
**Output Format**

Print the value of  *[SVG image]* .   

In the case of *ZeroDivisionError* or *ValueError*, print the error code.

**Sample Input**


```
3
1 0
2 $
3 1

```
**Sample Output**


```
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3

```

 **Note:**   

For integer division in **Python 3** use `//`.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Exceptions](./exceptions.py)

| Submissions                                                                     |                                     Leaderboard                                      |                                                                     Discussions |                                                                 Editorial |
| :------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------: | ------------------------------------------------------------------------------: | ------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/exceptions/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/exceptions/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/exceptions/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/exceptions/editorial) |

