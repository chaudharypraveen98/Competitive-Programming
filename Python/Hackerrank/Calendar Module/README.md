## [Calendar Module](https://www.hackerrank.com/challenges/calendar-module)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 97.01%        |

### **[Calendar Module](https://docs.python.org/2/library/calendar.html#module-calendar)**


The calendar module allows you to output calendars and provides additional useful functions for them.


**[class calendar.TextCalendar(\[firstweekday])](https://docs.python.org/2/library/calendar.html#calendar.TextCalendar)**


This class can be used to generate plain text calendars.


**Sample Code**



```
>>> import calendar
>>> 
>>> print calendar.TextCalendar(firstweekday=6).formatyear(2015)
                                  2015

      January                   February                   March
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
             1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
25 26 27 28 29 30 31                                29 30 31

       April                      May                       June
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
          1  2  3  4                      1  2          1  2  3  4  5  6
 5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
                          31

        July                     August                  September
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
          1  2  3  4                         1             1  2  3  4  5
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
                          30 31

      October                   November                  December
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
             1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
25 26 27 28 29 30 31      29 30                     27 28 29 30 31

```

To learn more about different calendar functions, [click here](https://docs.python.org/2/library/calendar.html#calendar.setfirstweekday).




---


**Task**


You are given a date. Your task is to find what the *day* is on that date.

**Input Format**

A single line of input containing the space separated month, day and year, respectively, in  *[SVG image]*   *[SVG image]*   *[SVG image]*  format.

**Constraints**

* *[SVG image]*
**Output Format**

Output the correct day in capital letters. 

**Sample Input**


```
08 05 2015

```
**Sample Output**


```
WEDNESDAY

```
**Explanation**

The day on August  *[SVG image]* th  *[SVG image]*  was `WEDNESDAY`.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Calendar Module](./calendar_module.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/calendar-module/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/calendar-module/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/calendar-module/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/calendar-module/editorial) |

