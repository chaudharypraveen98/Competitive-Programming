## [Java Dequeue](https://www.hackerrank.com/challenges/java-dequeue)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Medium       | 20      | 83.74%        |

In computer science, a double\-ended queue (dequeue, often abbreviated to deque, pronounced deck) is an abstract data type that generalizes a queue, for which elements can be added to or removed from either the front (head) or back (tail).


Deque interfaces can be implemented using various types of collections such as `LinkedList` or `ArrayDeque` classes. For example, deque can be declared as:



```
Deque deque = new LinkedList<>();
or
Deque deque = new ArrayDeque<>();

```

You can find more details about Deque [here](http://docs.oracle.com/javase/7/docs/api/java/util/Deque.html).


In this problem, you are given  *[SVG image]*  integers. You need to find the maximum number of unique integers among all the possible contiguous subarrays of size  *[SVG image]* .


*Note*: Time limit is  *[SVG image]*  second for this problem.

**Input Format**

The first line of input contains two integers  *[SVG image]*  and  *[SVG image]* : representing the total number of integers and the size of the subarray, respectively. The next line contains  *[SVG image]*  space separated integers. 


**Constraints**


 *[SVG image]*   

 *[SVG image]*   

 *[SVG image]*   

The numbers in the array will range between  *[SVG image]* .

**Output Format**

Print the *maximum* number of unique integers among all possible contiguous subarrays of size  *[SVG image]* .

**Sample Input**


```
6 3
5 3 5 2 3 2

```
**Sample Output**


```
3

```
**Explanation**

In the sample testcase, there are 4 subarrays of contiguous numbers.


 *[SVG image]*  \- Has  *[SVG image]*  unique numbers.


 *[SVG image]*  \- Has  *[SVG image]*  unique numbers.


 *[SVG image]*  \- Has  *[SVG image]*  unique numbers.


 *[SVG image]*  \- Has  *[SVG image]*  unique numbers.


In these subarrays, there are  *[SVG image]*  unique numbers, respectively. The maximum amount of unique numbers among all possible contiguous subarrays is  *[SVG image]* .


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Dequeue](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-dequeue/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-dequeue/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-dequeue/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-dequeue/editorial) |

