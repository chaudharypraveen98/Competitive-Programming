## [DefaultDict Tutorial](https://www.hackerrank.com/challenges/defaultdict-tutorial)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        92.82% |

The *defaultdict* tool is a container in the collections class of Python. It's similar to the usual dictionary (*dict*) container, but the only difference is that a defaultdict will have a *default* value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.   

**For example:**



```
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

```

This prints:
```
('python', ['awesome', 'language'])
('something-else', ['not relevant'])
```

In this challenge, you will be given  *[SVG image]*  integers,  *[SVG image]*  and  *[SVG image]* . There are  *[SVG image]*  words, which might repeat, in word group  *[SVG image]* . There are  *[SVG image]*  words belonging to word group  *[SVG image]* . For each  *[SVG image]*  words, check whether the word has appeared in group  *[SVG image]*  or not. Print the indices of each occurrence of  *[SVG image]*  in group  *[SVG image]* . If it does not appear, print  *[SVG image]* .


**Example** 


Group A contains 'a', 'b', 'a'
Group B contains 'a', 'c'


For the first word in group B, 'a', it appears at positions  *[SVG image]*  and  *[SVG image]*  in group A.
The second word, 'c', does not appear in group A, so print  *[SVG image]* .


Expected output:



```
1 3
-1

```
**Input Format**

The first line contains integers,  *[SVG image]*  and  *[SVG image]*  separated by a space.   

The next  *[SVG image]*  lines contains the words belonging to group  *[SVG image]* .   

The next  *[SVG image]*  lines contains the words belonging to group  *[SVG image]* .

**Constraints**

 *[SVG image]*    

 *[SVG image]*    

 *[SVG image]* 

**Output Format**

Output  *[SVG image]*  lines.   

The  *[SVG image]*  line should contain the  *[SVG image]* \-indexed positions of the occurrences of the  *[SVG image]*  word separated by spaces. 

**Sample Input**


```
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
```
**Sample Output**

```
1 2 4
3 5
```
**Explanation**
'a' appeared `3` times in positions `1`,`2` and `4`.
'b' appeared `2` times in positions `3` and `5`.
In the sample problem, if 'c' also appeared in word group `B`, you would print `-1`.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : DefaultDict Tutorial](./defaultdict_tutorial.py)

| Submissions                                                                               |                                          Leaderboard                                           |                                                                               Discussions |                                                                           Editorial |
| :---------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/defaultdict-tutorial/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/defaultdict-tutorial/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/defaultdict-tutorial/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/defaultdict-tutorial/editorial) |

