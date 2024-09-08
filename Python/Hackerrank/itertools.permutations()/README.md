## [itertools.permutations()](https://www.hackerrank.com/challenges/itertools-permutations)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    10     |        97.82% |

**[itertools.permutations(iterable\[, r])](https://docs.python.org/2/library/itertools.html#itertools.permutations)**


This tool returns successive **r** length permutations of elements in an iterable.

If **r** is not specified or is None, then **r** defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.


**Sample Code**



```
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

```

#### Task

You are given a string **S**.
Your task is to print all possible permutations of size **K** of the string in lexicographic sorted order.

#### Input Format

A single line containing the space separated string **S** and the integer value **K**.

#### Constraints

The string contains only UPPERCASE characters.

#### Output Format

Print the permutations of the string **S** on separate lines.

**Sample Input**


```
HACK 2

```
**Sample Output**


```
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

```
**Explanation**

All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : itertools.permutations()](./itertoolspermutations.py)

| Submissions                                                                                 |                                           Leaderboard                                            |                                                                                 Discussions |                                                                             Editorial |
| :------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/itertools-permutations/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/itertools-permutations/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/itertools-permutations/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/itertools-permutations/editorial) |

