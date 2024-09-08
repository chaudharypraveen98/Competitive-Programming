## [XML2 - Find the Maximum Depth](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 20      | 97.13%        |

You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as *0*.

#### Input Format
The first line contains *N*, the number of lines in the XML document.
The next *N* lines follow containing the XML document.
#### Output Format
Output a single line, the integer value of the maximum level of nesting in the XML document.


#### Sample Input
```
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
```

#### Sample Output
`1`

#### Explanation
Here, the root is a feed tag, which has depth of *0*.
The tags title, subtitle, link and updated all have a depth of *1*.

Thus, the maximum depth is *1*.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : XML2 - Find the Maximum Depth](./xml2__find_the_maximum_depth.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/editorial) |

