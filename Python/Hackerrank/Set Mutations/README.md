## [Set Mutations](https://www.hackerrank.com/challenges/py-set-mutations)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 98.16%        |

We have seen the applications of *union, intersection, difference* and *symmetric difference* operations, but these operations do not make any changes or mutations to the set. 


**We can use the following operations to create mutations to a set:**


**.update()** or **`|=`**   

Update the set by adding elements from an iterable/another set.  




```
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

```

**.intersection\_update()** or **`&=`**  

Update the set by keeping only the elements found in it and an iterable/another set.  




```
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])

```

**.difference\_update()** or **`-=`**  

Update the set by removing elements found in an iterable/another set.  




```
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])

```

**.symmetric\_difference\_update()** or **`^=`**  

Update the set by only keeping the elements found in either set, but not in both.



```
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])

```



---


**TASK**  

You are given a set  *[SVG image]*  and  *[SVG image]*  number of other sets. These  *[SVG image]*  number of sets have to perform some specific mutation operations on set  *[SVG image]* .


Your task is to execute those operations and print the sum of elements from set  *[SVG image]* .

**Input Format**

The first line contains the number of elements in set  *[SVG image]* .  

The second line contains the space separated list of elements in set  *[SVG image]* .  

The third line contains integer  *[SVG image]* , the number of other sets.  

The next  *[SVG image]*  lines are divided into  *[SVG image]*  parts containing two lines each.  

The first line of each part contains the space separated entries of the *operation name* and the *length of the other set*.  

The second line of each part contains space separated list of elements in the other set.  



 *[SVG image]*  *len(set(**A**))*  *[SVG image]*    

 *[SVG image]*  *len(otherSets)*  *[SVG image]*    

 *[SVG image]* 

**Output Format**

Output the sum of elements in set  *[SVG image]* .

**Sample Input**


```
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

```
**Sample Output**


```
38

```
**Explanation**

After the first operation, (*intersection\_update operation*), we get:  

set  *[SVG image]*   



After the second operation, (*update operation*), we get:  

set  *[SVG image]*   



After the third operation, (*symmetric\_difference\_update operation*), we get:  

set  *[SVG image]*   



After the fourth operation, ( *difference\_update operation*), we get:  

set  *[SVG image]*   



The sum of elements in set  *[SVG image]*  after these operations is  *[SVG image]* .


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Set Mutations](./set_mutations.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/py-set-mutations/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/py-set-mutations/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/py-set-mutations/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/py-set-mutations/editorial) |

