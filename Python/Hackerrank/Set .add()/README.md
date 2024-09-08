## [Set .add()](https://www.hackerrank.com/challenges/py-set-add)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 98.92%        |

If we want to add a single element to an existing set, we can use the *.add()* operation.   

It adds the element to the set and returns '**`None`**'.


**Example**



```
>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

```

  

**Task** 


Apply your knowledge of the *.add()* operation to help your friend Rupal.  
  

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  *[SVG image]*  country stamps.  
  

Find the total number of distinct country stamps.

**Input Format**

The first line contains an integer  *[SVG image]* , the total number of country stamps.  

The next  *[SVG image]*  lines contains the name of the country where the stamp is from.   
 


**Constraints** 


 *[SVG image]* 

**Output Format**

Output the total number of distinct country stamps on a single line.

**Sample Input**


```
7
UK
China
USA
France
New Zealand
UK
France 

```
**Sample Output**


```
5

```
**Explanation**

UK and France repeat twice. Hence, the total number of distinct country stamps is  *[SVG image]*  (five).


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Set .add()](./set_add.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/py-set-add/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/py-set-add/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/py-set-add/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/py-set-add/editorial) |

