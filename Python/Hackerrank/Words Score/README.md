## [Words Score](https://www.hackerrank.com/challenges/words-score)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Medium     |    10     |        94.86% |

In this challenge, the task is to debug the existing code to successfully execute all provided test files.




---


Consider that vowels in the alphabet are `a, e, i, o, u` and `y`. 


Function `score_words` takes a list of lowercase words as an argument and returns a score as follows:


The score of a single word is  *[SVG image]*  if the word contains an even number of vowels. Otherwise, the score of this word is  *[SVG image]* . The score for the whole list of words is the sum of scores of all words in the list. 


Debug the given function `score_words` such that it returns a correct score.


Your function will be tested on several cases by the locked template code.

**Input Format**

The input is read by the provided locked code template. In the first line, there is a single integer *n* denoting the number of words. In the second line, there are *n* space-separated lowercase words.

**Constraints**

* *[SVG image]*
* Each word has at most  *[SVG image]*  letters and all letters are English lowercase letters
**Output Format**

The output is produced by the provided and locked code template. It calls function `score_words` with the list of words read from the input as the argument and prints the returned score to the output.

**Sample Input 0**


```
2
hacker book

```

**Sample Output 0**


```
4

```

**Explanation 0**

There are two words in the input: hacker and book. The score of the word hacker is *2* because it contains an even number of vowels, i.e. *2* vowels, and the score of book is  for the same reason. Thus the total score is *2 + 2 = 4*.

**Sample Input 1**


```
3
programming is awesome

```

**Sample Output 1**


```
4

```

**Explanation 1**
There are *3* words in the input: programming, is and awesome. The score of programming is *1* since it contains *3* vowels, an odd number of vowels. The score of is is also *1* because it has an odd number of vowels. The score of awesome is *2* since it contains *4* vowels, an even number of vowels. Thus, the total score is *1 + 1 + 2 = 4*.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Words Score](./words_score.py)

| Submissions                                                                      |                                      Leaderboard                                      |                                                                      Discussions |                                                                  Editorial |
| :------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------------: | -------------------------------------------------------------------------------: | -------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/words-score/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/words-score/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/words-score/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/words-score/editorial) |

