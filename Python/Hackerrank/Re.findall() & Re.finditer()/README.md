## [Re.findall() & Re.finditer()](https://www.hackerrank.com/challenges/re-findall-re-finditer)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        93.16% |

### [re.findall()](https://docs.python.org/2/library/re.html#re.findall)


The expression *re.findall()* returns all the non\-overlapping matches of patterns in a string as a list of strings.   

**Code**



```
>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

```

### [re.finditer()](https://docs.python.org/2/library/re.html#re.finditer)


The expression *re.finditer()* returns an iterator yielding `MatchObject` instances over all non\-overlapping matches for the *re* pattern in the string.   

**Code**



```
>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

```



---


**Task**   

You are given a string  *[SVG image]* . It consists of alphanumeric characters, spaces and symbols(`+`,`-`).   

Your task is to find all the substrings of  *[SVG image]*  that contains  *[SVG image]*  or more vowels.   

Also, these substrings must lie in between  *[SVG image]*  consonants and should contain vowels only.


**Note :   

Vowels are defined as: `AEIOU` and `aeiou`.   

Consonants are defined as: `QWRTYPSDFGHJKLZXCVBNM` and `qwrtypsdfghjklzxcvbnm`**.

**Input Format**

A single line of input containing string  *S* .


**Constraints**


 *[SVG image]* 

**Output Format**

Print the matched substrings in their order of occurrence on separate lines.   

If no match is found, print `-1`.

**Sample Input**


```
rabcdeefgyYhFjkIoomnpOeorteeeeet

```
**Sample Output**


```
ee
Ioo
Oeo
eeeee

```
**Explanation**
**ee** is located between consonant d and f.
**Ioo** is located between consonant h and j.
**Oeo** is located between consonant m and p.
**eeeee** is located between consonant d and f.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Re.findall() & Re.finditer()](./refindall__refinditer.py)

| Submissions                                                                                 |                                           Leaderboard                                            |                                                                                 Discussions |                                                                             Editorial |
| :------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/re-findall-re-finditer/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/re-findall-re-finditer/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/re-findall-re-finditer/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/re-findall-re-finditer/editorial) |

