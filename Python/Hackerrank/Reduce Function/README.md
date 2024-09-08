## [Reduce Function](https://www.hackerrank.com/challenges/reduce-function)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Medium     |    30     |        98.27% |

Given a list of rational numbers,find their product. 


**Concept**   

The `reduce()` function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say `[1,2,3]` and you have to find its sum.



```
>>> reduce(lambda x, y : x + y,[1,2,3])
6

```

You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:



```
>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

>>> from fractions import gcd
>>> reduce(gcd, [2,4,8], 3)
1

```

**Input Format**

First line contains ,`n` the number of rational numbers.
The `ith` of next `n` lines contain two integers each, the numerator( `Ni` ) and denominator( `Di` ) of the `ith` rational number in the list.

**Constraints**

* *[SVG image]*
* *[SVG image]*
**Output Format**

Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than  `1` .

**Sample Input 0**


```
3
1 2
3 4
10 6

```

**Sample Output 0**


```
5 8

```

**Explanation 0**

Required product is 1/2*3/4*10/6 = 5/8


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Reduce Function](./reduce_function.py)

| Submissions                                                                          |                                        Leaderboard                                        |                                                                          Discussions |                                                                      Editorial |
| :----------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------: | -----------------------------------------------------------------------------------: | -----------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/reduce-function/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/reduce-function/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/reduce-function/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/reduce-function/editorial) |

