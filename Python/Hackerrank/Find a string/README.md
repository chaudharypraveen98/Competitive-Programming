## [Find a string](https://www.hackerrank.com/challenges/find-a-string)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    10     |        94.04% |

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. 


**NOTE:** String letters are case\-sensitive.


**Input Format** 


The first line of input contains the original string. The next line contains the substring.


**Constraints** 


 *[SVG image]*    

Each character in the string is an *ascii* character. 


**Output Format** 


Output the integer number indicating the total number of occurrences of the substring in the original string. 


**Sample Input**



```
ABCDCDC
CDC

```

**Sample Output**



```
2

```

**Concept**


Some string processing examples, [such as these](http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation), might be useful.   

There are a couple of new concepts:   

In Python, the length of a string is found by the function `len(s)`, where  *[SVG image]*  is the string.   

To traverse through the length of a string, use a *for* loop: 



```
for i in range(0, len(s)):
    print (s[i])

```

A range function is used to loop over some length: 



```
range (0, 5)

```

Here, the range loops over 0 to **4.5**  is excluded.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Find a string](./find_a_string.py)

| Submissions                                                                        |                                       Leaderboard                                       |                                                                        Discussions |                                                                    Editorial |
| :--------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------: | ---------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/find-a-string/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/find-a-string/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/find-a-string/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/find-a-string/editorial) |

