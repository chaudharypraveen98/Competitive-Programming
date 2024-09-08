## [Re.start() & Re.end()](https://www.hackerrank.com/challenges/re-start-re-end)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 20      | 93.98%        |

### [start() \& end()](https://docs.python.org/2/library/re.html#re.MatchObject.start)


These expressions return the indices of the *start* and *end* of the substring matched by the group.


**Code** 



```
>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0

```



---


**Task**   

You are given a string  *[SVG image]* .   

Your task is to find the indices of the *start* and *end* of string  *[SVG image]*  in  *[SVG image]* .

**Input Format**

The first line contains the string  *[SVG image]* .   

The second line contains the string  *[SVG image]* .


**Constraints** 


 *[SVG image]*    

 *[SVG image]* 

**Output Format**

Print the tuple in this format: (*start* \_*index*, *end* \_*index*).   

If no match is found, print `(-1, -1)`.

**Sample Input**


```
aaadaa
aa

```
**Sample Output**


```
(0, 1)  
(1, 2)
(4, 5)

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Re.start() & Re.end()](./restart__reend.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/re-start-re-end/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/re-start-re-end/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/re-start-re-end/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/re-start-re-end/editorial) |

