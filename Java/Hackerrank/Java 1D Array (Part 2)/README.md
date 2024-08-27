## [Java 1D Array (Part 2)](https://www.hackerrank.com/challenges/java-1d-array)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Medium       | 25      | 72.28%        |

Let's play a game on an array! You're standing at index  *[SVG image]*  of an  *[SVG image]* \-element array named  *[SVG image]* . From some index  *[SVG image]*  (where  *[SVG image]* ), you can perform one of the following moves:


* *Move Backward:* If cell  *[SVG image]*  exists *and* contains a  *[SVG image]* , you can walk back to cell  *[SVG image]* .
* *Move Forward:*
	+ If cell  *[SVG image]*  contains a zero, you can walk to cell  *[SVG image]* .
	+ If cell  *[SVG image]*  contains a zero, you can jump to cell  *[SVG image]* .
	+ If you're standing in cell  *[SVG image]*  or the value of  *[SVG image]* , you can walk or jump off the end of the array and win the game.


In other words, you can move from index  *[SVG image]*  to index  *[SVG image]* ,  *[SVG image]* , or  *[SVG image]*  as long as the destination index is a cell containing a  *[SVG image]* . If the destination index is greater than  *[SVG image]* , you win the game.


**Function Description** 


Complete the *canWin* function in the editor below. 


*canWin* has the following parameters: 


* *int leap:* the size of the leap
* *int game\[n]:* the array to traverse


**Returns** 


* *boolean:* true if the game can be won, otherwise false
**Input Format**

The first line contains an integer,  *[SVG image]* , denoting the number of queries (i.e., function calls).   

The  *[SVG image]*  subsequent lines describe each query over two lines:


1. The first line contains two space\-separated integers describing the respective values of  *[SVG image]*  and  *[SVG image]* .
2. The second line contains  *[SVG image]*  space\-separated binary integers (i.e., zeroes and ones) describing the respective values of  *[SVG image]* .
**Constraints**

* *[SVG image]*
* *[SVG image]*
* *[SVG image]*
* It is guaranteed that the value of  *[SVG image]*  is always  *[SVG image]* .
**Sample Input**


```
STDIN           Function
-----           --------
4               q = 4 (number of queries)
5 3             game[] size n = 5, leap = 3 (first query)
0 0 0 0 0       game = [0, 0, 0, 0, 0]
6 5             game[] size n = 6, leap = 5 (second query)
0 0 0 1 1 1     . . .
6 3
0 0 1 1 1 0
3 1
0 1 0

```
**Sample Output**


```
YES
YES
NO
NO

```
**Explanation**

We perform the following  *[SVG image]*  queries:


1. For  *[SVG image]*  and  *[SVG image]* , we can walk and/or jump to the end of the array because every cell contains a  *[SVG image]* . Because we can win, we return *true*.
2. For  *[SVG image]*  and  *[SVG image]* , we can walk to index  *[SVG image]*  and then jump  *[SVG image]*  units to the end of the array. Because we can win, we return *true*.
3. For  *[SVG image]*  and  *[SVG image]* , there is no way for us to get past the three consecutive ones. Because we cannot win, we return *false*.
4. For  *[SVG image]*  and  *[SVG image]* , there is no way for us to get past the one at index  *[SVG image]* . Because we cannot win, we return *false*.

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java 1D Array (Part 2)](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-1d-array/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-1d-array/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-1d-array/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-1d-array/editorial) |

