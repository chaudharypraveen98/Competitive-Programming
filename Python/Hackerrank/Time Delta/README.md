## [Time Delta](https://www.hackerrank.com/challenges/python-time-delta)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Medium     |    30     |        91.40% |

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago. 


Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format: 


`Day dd Mon yyyy hh:mm:ss +xxxx`


Here \+xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them. 

**Input Format**

The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and time t2.

**Constraints**

* Input contains only valid timestamps
* *[SVG image]* .
**Output Format**

Print the absolute difference t1-t2 in seconds.

**Sample Input 0**


```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

```

**Sample Output 0**


```
25200
88200

```

**Explanation 0**

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7x3600 seconds or 25200 seconds.



Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes Or 24x3600 +30x60 => 88200


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Time Delta](./time_delta.py)

| Submissions                                                                            |                                         Leaderboard                                         |                                                                            Discussions |                                                                        Editorial |
| :------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/python-time-delta/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/python-time-delta/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/python-time-delta/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/python-time-delta/editorial) |

