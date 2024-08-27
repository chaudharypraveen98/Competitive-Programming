## [Java SHA-256](https://www.hackerrank.com/challenges/sha-256)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Medium       | 30      | 96.33%        |

Cryptographic hash functions are mathematical operations run on digital data; by comparing the computed *hash* (i.e., the output produced by executing a hashing algorithm) to a known and expected hash value, a person can determine the data's integrity. For example, computing the hash of a downloaded file and comparing the result to a previously published hash result can show whether the download has been modified or tampered with. In addition, cryptographic hash functions are extremely collision\-resistant; in other words, it should be extremely difficult to produce the same hash output from two different input values using a cryptographic hash function.


*Secure Hash Algorithm 2* (*SHA\-2*) is a set of cryptographic hash functions designed by the National Security Agency (NSA). It consists of six identical hashing algorithms (i.e., *SHA\-256*, *SHA\-512*, *SHA\-224*, *SHA\-384*, *SHA\-512/224*, *SHA\-512/256*) with a variable digest size. *SHA\-256* is a  *[SVG image]* \-bit ( *[SVG image]*  byte) hashing algorithm which can calculate a hash code for an input of up to  *[SVG image]*  bits. It undergoes  *[SVG image]*  rounds of hashing and calculates a hash code that is a  *[SVG image]* \-digit hexadecimal number.


Given a string,  *[SVG image]* , print its *SHA\-256* hash value.

**Input Format**

A single alphanumeric string denoting  *[SVG image]* .

**Constraints**

* *[SVG image]*
* String  *[SVG image]*  consists of English alphabetic letters (i.e.,  *[SVG image]*  and/or decimal digits (i.e.,  *[SVG image]*  through  *[SVG image]* ) only.
**Output Format**

Print the *SHA\-256* encryption value of  *[SVG image]*  on a new line. 


**Sample Input 0**



```
HelloWorld

```

**Sample Output 0**



```
872e4e50ce9990d8b041330c47c9ddd11bec6b503ae9386a99da8584e9bb12c4

```

**Sample Input 1**



```
Javarmi123

```

**Sample Output 1**



```
f1d5f8d75bb55c777207c251d07d9091dc10fe7d6682db869106aacb4b7df678

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java SHA-256](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/sha-256/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/sha-256/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/sha-256/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/sha-256/editorial) |

