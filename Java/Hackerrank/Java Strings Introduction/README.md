## [Java Strings Introduction](https://www.hackerrank.com/challenges/java-strings-introduction)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 5      | 93.78%        |


> "A string is traditionally a sequence of characters, either as a literal constant or as some kind of variable." — [Wikipedia: String (computer science)](https://en.wikipedia.org/wiki/String_%28computer_science%29)


This exercise is to test your understanding of Java Strings. A sample *String* declaration:



```
String myString = "Hello World!"

```

The elements of a *String* are called *characters*. The number of *characters* in a *String* is called the *length*, and it can be retrieved with the *String.length()* method.


Given two strings of lowercase English letters,  *[SVG image]*  and  *[SVG image]* , perform the following operations:


1. Sum the lengths of  *[SVG image]*  and  *[SVG image]* .
2. Determine if  *[SVG image]*  is lexicographically larger than  *[SVG image]*  (i.e.: does  *[SVG image]*  come before  *[SVG image]*  in the dictionary?).
3. Capitalize the first letter in  *[SVG image]*  and  *[SVG image]*  and print them on a single line, separated by a space.
**Input Format**

The first line contains a string  *[SVG image]* .
The second line contains another string  *[SVG image]* .
The strings are comprised of only lowercase English letters.

**Output Format**

There are three lines of output:   

For the first line, sum the lengths of  *[SVG image]*  and  *[SVG image]* .   

For the second line, write `Yes` if  *[SVG image]*  is lexicographically greater than  *[SVG image]*  otherwise print `No` instead.   

For the third line, capitalize the first letter in both  *[SVG image]*  and  *[SVG image]*  and print them on a single line, separated by a space.

**Sample Input 0**


```
hello
java

```

**Sample Output 0**


```
9
No
Hello Java

```

**Explanation 0**

String  *[SVG image]*  is "hello" and  *[SVG image]*  is "java". 


 *[SVG image]*  has a *length* of  *[SVG image]* , and  *[SVG image]*  has a *length* of  *[SVG image]* ; the sum of their lengths is  *[SVG image]* .   

When sorted alphabetically/lexicographically, "hello" precedes "java"; therefore,  *[SVG image]*  is not greater than  *[SVG image]*  and the answer is `No`. 


When you capitalize the first letter of both  *[SVG image]*  and  *[SVG image]*  and then print them separated by a space, you get "Hello Java".


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Strings Introduction](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-strings-introduction/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-strings-introduction/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-strings-introduction/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-strings-introduction/editorial) |

