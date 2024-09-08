## [Set .discard(), .remove() & .pop()](https://www.hackerrank.com/challenges/py-set-discard-remove-pop)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    10     |        93.49% |

**.remove(x)**  
This operation removes element **x** from the set.
If element **x** does not exist, it raises a <strong><code>KeyError</code></strong>.
The <em>.remove(x)</em> operation returns <strong><code>None</code></strong>.


**Example**



```
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0

```



---


**.discard(x)**  
This operation also removes element **x** from the set.
If element **x** does not exist, it <strong>does not</strong> raise a <code>KeyError</code>.
The <em>.discard(x)</em> operation returns <strong><code>None</code></strong>.


**Example**



```
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])

```



---


**.pop()**  
 


This operation removes and return an arbitrary element from the set.   

If there are no elements to remove, it raises a **`KeyError`**.


**Example**



```
>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set

```



---


**Task**  
You have a non-empty set **s**, and you have to execute **N** commands given in **N** lines.

The commands will be pop, remove and discard.

**Input Format**
The first line contains integer **n**, the number of elements in the set **s**.
The second line contains **N** space separated elements of set **s**. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer **N**, the number of commands.
The next **N** lines contains either pop, remove and/or discard commands followed by their associated value.


**Constraints**


 *[SVG image]*    

 *[SVG image]* 

**Output Format**
Print the sum of the elements of set **s** on a single line.

**Sample Input**


```
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

```
**Sample Output**


```
4

```
**Explanation**

After completing these 10 operations on the set([4]) ,we get set. Hence, the sum is 4.

Note: Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Set .discard(), .remove() & .pop()](./set_discard_remove__pop.py)

| Submissions                                                                                    |                                             Leaderboard                                             |                                                                                    Discussions |                                                                                Editorial |
| :--------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/editorial) |

