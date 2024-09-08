## [Detect Floating Point Number](https://www.hackerrank.com/challenges/introduction-to-regex)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        92.72% |

Check [Tutorial](https://www.hackerrank.com/challenges/introduction-to-regex/tutorial) tab to know how to to solve. 


You are given a string  *[SVG image]* .   

Your task is to verify that  *[SVG image]*  is a floating point number. 


In this task, a valid float number must satisfy *all* of the following requirements: 


 *[SVG image]*  Number can start with **`+`**, **`-`** or **`.`** symbol.   

 *[SVG image]* For example:   

 *[SVG image]* \+4\.50   

 *[SVG image]* \-1\.0   

 *[SVG image]* .5   

 *[SVG image]* \-.7   

 *[SVG image]* \+.4   

 *[SVG image]*  **`-+4.5`** 


 *[SVG image]*  Number must contain *at least*  *[SVG image]*  decimal value.   

 *[SVG image]* For example:   

 *[SVG image]*  **`12.`**   

 *[SVG image]* 12\.0   


 *[SVG image]*  Number must have exactly one **`.`** symbol.   

 *[SVG image]*  Number must not give any exceptions when converted using  *[SVG image]* .

**Input Format**

The first line contains an integer  *[SVG image]* , the number of test cases.   

The next  *[SVG image]*  line(s) contains a string  *[SVG image]* .

**Constraints**

* *[SVG image]*
**Output Format**

Output *True* or *False* for each test case.

**Sample Input 0**


```
4
4.0O0
-1.00
+4.54
SomeRandomStuff

```

**Sample Output 0**


```
False
True
True
False

```

**Explanation 0**  
*4.0O0*: O is not a digit.
*-1.00*: is valid.
*+4.54*: is valid.
SomeRandomStuff: is not a number.



## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Detect Floating Point Number](./detect_floating_point_number.py)

| Submissions                                                                                |                                           Leaderboard                                           |                                                                                Discussions |                                                                            Editorial |
| :----------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------: | -----------------------------------------------------------------------------------------: | -----------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/introduction-to-regex/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/introduction-to-regex/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/introduction-to-regex/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/introduction-to-regex/editorial) |

