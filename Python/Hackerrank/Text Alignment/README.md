## [Text Alignment](https://www.hackerrank.com/challenges/text-alignment)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 96.71%        |

In Python, a string of text can be aligned *left, right* and *center*.


**.ljust(width)**


This method returns a left aligned string of length *width*.



```
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  

```



---


**.center(width)**


This method returns a centered string of length *width*.



```
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----

```



---


**.rjust(width)**


This method returns a right aligned string of length *width*.



```
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank

```



---


**Task**


You are given a partial code that is used for generating the *HackerRank Logo* of variable *thickness*.   

Your task is to replace the blank (`______`) with *rjust, ljust* or *center*.

**Input Format**

A single line containing the *thickness* value for the logo.


**Constraints** 


The *thickness* must be an *odd* number.   

 *[SVG image]* 

**Output Format**

Output the desired logo.

**Sample Input**


```
5

```
**Sample Output**


```
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Text Alignment](./text_alignment.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/text-alignment/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/text-alignment/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/text-alignment/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/text-alignment/editorial) |

