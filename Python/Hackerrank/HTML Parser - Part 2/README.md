## [HTML Parser - Part 2](https://www.hackerrank.com/challenges/html-parser-part-2)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 30      | 97.84%        |

`*`This section assumes that you understand the basics discussed in **HTML Parser \- Part 1**


[*.handle\_comment(data)*](https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser.handle_comment)   

This method is called when a comment is encountered (e.g. \<!\-\-comment\-\-\>).   

The *data* argument is the content inside the comment tag:



```
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
          print "Comment  :", data

```

  



[*.handle\_data(data)*](https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser.handle_data)   

This method is called to process arbitrary data (e.g. text nodes and the content of \<script\>...\</script\> and \<style\>...\</style\>).   

The *data* argument is the text content of HTML.



```
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print "Data     :", data

```



---


**Task**


You are given an *HTML* code snippet of  *[SVG image]*  lines.   

Your task is to print the *single\-line comments, multi\-line comments* and the *data*. 


Print the result in the following format:



```
>>> Single-line Comment  
Comment
>>> Data                 
My Data
>>> Multi-line Comment  
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:  

```

**Note**: Do not print *data* if `data == '\n'`. 

**Input Format**

The first line contains integer  *[SVG image]* , the number of lines in the *HTML* code snippet.  

The next  *[SVG image]*  lines contains *HTML* code.


**Constraints**


 *[SVG image]* 

**Output Format**

Print the *single\-line comments, multi\-line comments* and the *data* in order of their occurrence from top to bottom in the snippet.  



Format the answers as explained in the problem statement.

**Sample Input**


```
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->

```
**Sample Output**


```
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : HTML Parser - Part 2](./html_parser__part_2.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/html-parser-part-2/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/html-parser-part-2/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/html-parser-part-2/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/html-parser-part-2/editorial) |

