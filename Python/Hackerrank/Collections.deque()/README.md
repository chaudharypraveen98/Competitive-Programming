## [Collections.deque()](https://www.hackerrank.com/challenges/py-collections-deque)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        97.99% |

A deque is a double-ended queue. It can be used to add or remove elements from both ends.<br>Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same performance in either direction.<br>Click on the link to learn more about deque() methods.
Click on the link to learn more about various approaches to working with deques: Deque Recipes.

Example  
Code  
```
>>> from collections import deque
>>> d = deque()
>>> d.append(1)
>>> print d
deque([1])
>>> d.appendleft(2)
>>> print d
deque([2, 1])
>>> d.clear()
>>> print d
deque([])
>>> d.extend('1')
>>> print d
deque(['1'])
>>> d.extendleft('234')
>>> print d
deque(['4', '3', '2', '1'])
>>> d.count('1')
1
>>> d.pop()
'1'
>>> print d
deque(['4', '3', '2'])
>>> d.popleft()
'4'
>>> print d
deque(['3', '2'])
>>> d.extend('7896')
>>> print d
deque(['3', '2', '7', '8', '9', '6'])
>>> d.remove('2')
>>> print d
deque(['3', '7', '8', '9', '6'])
>>> d.reverse()
>>> print d
deque(['6', '9', '8', '7', '3'])
>>> d.rotate(3)
>>> print d
deque(['8', '7', '3', '6', '9'])
```

**Task**  
Perform append, pop, popleft and appendleft methods on an empty deque `d`

**Input Format**  

The first line contains an integer `N`, the number of operations.
The next `N` lines contains the space separated names of methods and their values.

**Output Format**

Print the space separated elements of deque `d`.

**Sample Input 0**  
```
6
append 1
append 2
append 3
appendleft 4
pop
popleft
```

**Sample Output 0**  
`1 2`

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Collections.deque()](./collectionsdeque.py)

| Submissions                                                                               |                                          Leaderboard                                           |                                                                               Discussions |                                                                           Editorial |
| :---------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/py-collections-deque/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/py-collections-deque/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/py-collections-deque/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/py-collections-deque/editorial) |

