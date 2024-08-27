## [Java Comparator](https://www.hackerrank.com/challenges/java-comparator)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Medium       | 10      | 97.46%        |

Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array.


The *Player* class is provided for you in your editor. It has  *[SVG image]*  fields: a  *[SVG image]*  String and a  *[SVG image]*  integer.


Given an array of  *[SVG image]*  *Player* objects, write a comparator that sorts them in order of decreasing score; if  *[SVG image]*  or more players have the same score, sort those players alphabetically by name. To do this, you must create a *Checker* class that implements the *Comparator* interface, then write an *int compare(Player a, Player b)* method implementing the [Comparator.compare(T o1, T o2\)](https://docs.oracle.com/javase/7/docs/api/java/util/Comparator.html#compare%28T,%20T%29) method.

**Input Format**

Input from stdin is handled by the locked stub code in the *Solution* class. 


The first line contains an integer,  *[SVG image]* , denoting the number of players.   

Each of the  *[SVG image]*  subsequent lines contains a player's  *[SVG image]*  and  *[SVG image]* , respectively.

**Constraints**

* *[SVG image]*
* *[SVG image]*  players can have the same name.
* Player names consist of lowercase English letters.
**Output Format**

You are not responsible for printing any output to stdout. The locked stub code in *Solution* will create a *Checker* object, use it to sort the *Player* array, and print each sorted element.

**Sample Input**


```
5
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150

```
**Sample Output**


```
aleksa 150
amy 100
david 100
aakansha 75
heraldo 50

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Comparator](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-comparator/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-comparator/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-comparator/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-comparator/editorial) |

