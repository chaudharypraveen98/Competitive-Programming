## [Java String Reverse](https://www.hackerrank.com/challenges/java-string-reverse)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 97.82%        |

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. 




---


Given a string  *[SVG image]* , print `Yes` if it is a palindrome, print `No` otherwise. 

**Constraints**

* *[SVG image]*  will consist at most  *[SVG image]*  lower case english letters.
**Sample Input**


```
madam

```
**Sample Output**


```
Yes

```

## 💡 Hints 

### Problem Context

- The task is to determine if a given string is a palindrome.
- A palindrome is a string that reads the same forward and backward (e.g., "madam", "racecar").

#### Step 1 

- The code uses a `Scanner` object to read a single input string from the user
- **Hint**: You only need to check if this string is the same when reversed

#### Step 2

- The variable `isPalindrome` is initially set to true, assuming the string is a palindrome unless proven otherwise.
- **Hint**: You will loop through the string, comparing characters from the start and end towards the middle.

#### Step 3

- A for loop is used to iterate over the first half of the string (from index 0 to n/2 - 1).
- Hint: The length of the string is calculated using A.length().
- Hint: In each iteration, the characters at the current index i (from the start) and the character at index n-i-1 (from the end) are compared.

#### Step 4 

- If any pair of characters at these positions do not match, the string is not a palindrome:
- Hint: If a mismatch is found, set isPalindrome to false and break out of the loop early.

#### Step 5 

- After the loop, check the value of isPalindrome:
- If true, print "Yes" (the string is a palindrome).
- If false, print "No" (the string is not a palindrome).

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java String Reverse](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-string-reverse/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-string-reverse/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-string-reverse/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-string-reverse/editorial) |

