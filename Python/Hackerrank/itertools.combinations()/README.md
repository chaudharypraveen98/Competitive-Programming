## [itertools.combinations()](https://www.hackerrank.com/challenges/itertools-combinations)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    10     |        96.95% |

**[itertools.combinations(iterable, r)](https://docs.python.org/2/library/itertools.html#itertools.combinations)**   

This tool returns the  *[SVG image]*  length subsequences of elements from the input iterable.


Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.


 **Sample Code** 



```
>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

```



---


**Task**  
You are given a string ```S```.
Your task is to print all possible combinations, up to size ```k``` , of the string in lexicographic sorted order.

**Input Format**

A single line containing the string  *[SVG image]*  and integer value  *[SVG image]*  separated by a space.


**Constraints**


 *[SVG image]*    

The string contains only *UPPERCASE* characters.

**Output Format**

Print the different combinations of string  *[SVG image]*  on separate lines.

**Sample Input**


```
HACK 2

```
**Sample Output**


```
A
C
H
K
AC
AH
AK
CH
CK
HK

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : itertools.combinations()](./itertoolscombinations.py)

| Submissions                                                                                 |                                           Leaderboard                                            |                                                                                 Discussions |                                                                             Editorial |
| :------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/itertools-combinations/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/itertools-combinations/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/itertools-combinations/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/itertools-combinations/editorial) |

