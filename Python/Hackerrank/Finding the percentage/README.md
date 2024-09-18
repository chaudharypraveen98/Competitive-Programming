## [Finding the percentage](https://www.hackerrank.com/challenges/finding-the-percentage)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    10     |        97.28% |

The provided code stub will read in a dictionary containing key/value pairs of name:\[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal. 


**Example**   
```
marks key:value pairs are
'alpha':[20,30,40]
'beta':[30,50,70]
query_name = 'beta'
```


The **query\_name** is 'beta'. beta's average score is  *query_name* .

**Input Format**

The first line contains the integer `n`, the number of students' records. The next `n` lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

**Constraints**

* 2<=n<=10
* 0<=marks[i]<=100
* length of marks arrays = 3

**Output Format**

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

**Sample Input 0**


```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

```

**Sample Output 0**


```
56.00

```

**Explanation 0**

Marks for Malika are  *{52,56,60}*  whose average is  *52+56+60/3=>56* 

**Sample Input 1**


```
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

```

**Sample Output 1**


```
26.50

```


## 💡 Hints 
use key to query in dict

## ➡️ Approach 
Just get the item from the dict and sum and calculate percentage and print.

## ✅ Detailed Solution
[View Solution : Finding the percentage](./finding_the_percentage.py)

| Submissions                                                                                 |                                           Leaderboard                                            |                                                                                 Discussions |                                                                             Editorial |
| :------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/finding-the-percentage/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/finding-the-percentage/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/finding-the-percentage/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/finding-the-percentage/editorial) |

