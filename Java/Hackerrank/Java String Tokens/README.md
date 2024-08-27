## [Java String Tokens](https://www.hackerrank.com/challenges/java-string-tokens)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 15      | 82.41%        |

Given a string,  *[SVG image]* , matching the regular expression `[A-Za-z !,?._'@]+`, split the string into *tokens*. We define a token to be one or more consecutive English alphabetic letters. Then, print the number of tokens, followed by each token on a new line.


**Note:** You may find the [String.split](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#split-java.lang.String-) method helpful in completing this challenge.

**Input Format**

A single string,  *[SVG image]* .

**Constraints**

* *[SVG image]*
* *[SVG image]*  is composed of *any* of the following: English alphabetic letters, blank spaces, exclamation points (`!`), commas (`,`), question marks (`?`), periods (`.`), underscores (`_`), apostrophes (`'`), and at symbols (`@`).
**Output Format**

On the first line, print an integer,  *[SVG image]* , denoting the number of tokens in string  *[SVG image]*  (they *do not* need to be unique). Next, print each of the  *[SVG image]*  tokens on a new line in the same order as they appear in input string  *[SVG image]* .

**Sample Input**


```
He is a very very good boy, isn't he?

```
**Sample Output**


```
10
He
is
a
very
very
good
boy
isn
t
he

```
**Explanation**

We consider a token to be a contiguous segment of alphabetic characters. There are a total of  *[SVG image]*  such tokens in string  *[SVG image]* , and each token is printed in the same order in which it appears in string  *[SVG image]* .


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java String Tokens](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-string-tokens/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-string-tokens/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-string-tokens/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-string-tokens/editorial) |

