## [Java Substring Comparisons](https://www.hackerrank.com/challenges/java-string-compare)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 91.95%        |

We define the following terms:


* [Lexicographical Order](https://en.wikipedia.org/wiki/Lexicographical_order), also known as *alphabetic* or *dictionary* order, orders characters as follows:   



 *[SVG image]*  
For example, `ball < cat`, `dog < dorm`, `Happy < happy`, `Zoo < ball`.
* A [substring](https://en.wikipedia.org/wiki/Substring) of a string is a contiguous block of characters in the string. For example, the substrings of `abc` are `a`, `b`, `c`, `ab`, `bc`, and `abc`.


Given a string,  *[SVG image]* , and an integer,  *[SVG image]* , complete the function so that it finds the lexicographically *smallest* and *largest* substrings of length  *[SVG image]* . 


**Function Description** 


Complete the *getSmallestAndLargest* function in the editor below. 


*getSmallestAndLargest* has the following parameters: 


* *string s:* a string
* *int k:* the length of the substrings to find


**Returns** 


* *string:* the string ' \+ "\\n" \+ ' where and are the two substrings
**Input Format**

The first line contains a string denoting  *[SVG image]* .   

The second line contains an integer denoting  *[SVG image]* .

**Constraints**

* *[SVG image]*
* *[SVG image]*  consists of English alphabetic letters only (i.e., `[a-zA-Z]`).
**Sample Input 0**


```
welcometojava
3

```

**Sample Output 0**


```
ava
wel

```

**Explanation 0**

String  *[SVG image]*  has the following lexicographically\-ordered substrings of length  *[SVG image]* :


 *[SVG image]* 
We then return the first (lexicographically smallest) substring and the last (lexicographically largest) substring as two newline\-separated values (i.e., `ava\nwel`).


The stub code in the editor then prints `ava` as our first line of output and `wel` as our second line of output.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Substring Comparisons](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-string-compare/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-string-compare/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-string-compare/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-string-compare/editorial) |

