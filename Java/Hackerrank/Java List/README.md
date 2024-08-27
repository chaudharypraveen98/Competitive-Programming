## [Java List](https://www.hackerrank.com/challenges/java-list)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 15      | 95.78%        |

For this problem, we have  *[SVG image]*  types of queries you can perform on a [List](https://docs.oracle.com/javase/7/docs/api/java/util/List.html):


1. Insert  *[SVG image]*  at index  *[SVG image]* :  




```
Insert
x y
```
2. Delete the element at index  *[SVG image]* :  




```
Delete
x
```


Given a list,  *[SVG image]* , of  *[SVG image]*  integers, perform  *[SVG image]*  queries on the list. Once all queries are completed, print the modified list as a single line of space\-separated integers. 

**Input Format**

The first line contains an integer,  *[SVG image]*  (the initial number of elements in  *[SVG image]* ).   

The second line contains  *[SVG image]*  space\-separated integers describing  *[SVG image]* .   

The third line contains an integer,  *[SVG image]*  (the number of queries).   

The  *[SVG image]*  subsequent lines describe the queries, and each query is described over two lines: 


* If the first line of a query contains the String **Insert**, then the second line contains two space separated integers  *[SVG image]* , and the value  *[SVG image]*  must be inserted into  *[SVG image]*  at index  *[SVG image]* .
* If the first line of a query contains the String **Delete**, then the second line contains index  *[SVG image]* , whose element must be deleted from  *[SVG image]* .


**Constraints** 


* *[SVG image]*
* *[SVG image]*
* Each element in is a *32\-bit integer*.
**Output Format**

Print the updated list  *[SVG image]*  as a single line of space\-separated integers.

**Sample Input**


```
5
12 0 1 78 12
2
Insert
5 23
Delete
0

```
**Sample Output**


```
0 1 78 12 23

```
**Explanation**

 *[SVG image]*  


 *[SVG image]*  **Insert** 23 at index  *[SVG image]* .   

 *[SVG image]* 


 *[SVG image]*  **Delete** the element at index  *[SVG image]* .   

 *[SVG image]* 


Having performed all  *[SVG image]*  queries, we print  *[SVG image]*  as a single line of space\-separated integers.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java List](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-list/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-list/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-list/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-list/editorial) |

