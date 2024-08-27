## [Valid Username Regular Expression](https://www.hackerrank.com/challenges/valid-username-checker)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 20      | 95.74%        |

You are updating the username policy on your company's internal networking platform. According to the policy, a username is considered valid if all the following constraints are satisfied:


* The username consists of  *[SVG image]*  to  *[SVG image]*  characters inclusive. If the username consists of less than  *[SVG image]*  or greater than  *[SVG image]*  characters, then it is an invalid username.
* The username can only contain alphanumeric characters and underscores (`_`). Alphanumeric characters describe the character set consisting of *lowercase* characters  *[SVG image]* , *uppercase* characters  *[SVG image]* , and digits  *[SVG image]* .
* The *first* character of the username must be an *alphabetic* character, i.e., either *lowercase* character  *[SVG image]*  or *uppercase* character  *[SVG image]* .


For example:




| Username | Validity |
| --- | --- |
| *[SVG image]* | INVALID; Username length \< 8 characters |
| *[SVG image]* | VALID |
| *[SVG image]* | VALID |
| *[SVG image]* | INVALID; Username begins with non\-alphabetic character |
| *[SVG image]* | INVALID; '?' character not allowed |


Update the value of *regularExpression* field in the *UsernameValidator* class so that the regular expression only matches with valid usernames. 

**Input Format**

The first line of input contains an integer  *[SVG image]* , describing the total number of usernames. Each of the next  *[SVG image]*  lines contains a string describing the username. The locked stub code reads the inputs and validates the username.

**Constraints**

* *[SVG image]*
* The username consists of any printable characters.
**Output Format**

For each of the usernames, the locked stub code prints `Valid` if the username is valid; otherwise `Invalid` each on a new line.

**Sample Input 0**


```
8
Julia
Samantha
Samantha_21
1Samantha
Samantha?10_2A
JuliaZ007
Julia@007
_Julia007

```

**Sample Output 0**


```
Invalid
Valid
Valid
Invalid
Invalid
Valid
Invalid
Invalid

```

**Explanation 0**

Refer diagram in the challenge statement. 


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Valid Username Regular Expression](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/valid-username-checker/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/valid-username-checker/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/valid-username-checker/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/valid-username-checker/editorial) |

