## [Check Strict Superset](https://www.hackerrank.com/challenges/py-check-strict-superset)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    10     |        95.33% |

You are given a set  *[SVG image]*  and  *[SVG image]*  other sets.   

Your job is to find whether set  *[SVG image]*  is a strict superset of each of the  *[SVG image]*  sets. 


Print `True`, if  *[SVG image]*  is a *strict superset* of each of the  *[SVG image]*  sets. Otherwise, print `False`. 


A strict superset has at least one element that does not exist in its subset. 


**Example**   

Set *[SVG image]*  is a *strict superset* of set *[SVG image]* .   

Set *[SVG image]*  is not a *strict superset* of set *[SVG image]* .   

Set *[SVG image]*  is not a *strict superset* of set *[SVG image]* . 

**Input Format**

The first line contains the space separated elements of set  *[SVG image]* .   

The second line contains integer  *[SVG image]* , the number of other sets.   

The next  *[SVG image]*  lines contains the space separated elements of the other sets. 

**Constraints**

* *[SVG image]*
* *[SVG image]*
* *[SVG image]*
**Output Format**

Print `True` if set  *[SVG image]*  is a *strict superset* of all other  *[SVG image]*  sets. Otherwise, print `False`.

**Sample Input 0**
```
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
```

**Sample Output 0**
```
False
```

**Explanation 0**

Set **A** is the strict superset of the set `([1,2,3,4,5])` but not of the set ([100,11,12]) because **100** is not in set **A** . 

Hence, the output is `False`.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Check Strict Superset](./check_strict_superset.py)

| Submissions                                                                                   |                                            Leaderboard                                             |                                                                                   Discussions |                                                                               Editorial |
| :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/py-check-strict-superset/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/py-check-strict-superset/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/py-check-strict-superset/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/py-check-strict-superset/editorial) |

