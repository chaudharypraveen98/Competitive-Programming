## [Regex Substitution](https://www.hackerrank.com/challenges/re-sub-regex-substitution)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Medium       | 20      | 93.87%        |

The *re.sub()* tool (*sub* stands for *substitution*) evaluates a pattern and, for each valid match, it calls a *method* (or *lambda*).   

The *method* is called for all matches and can be used to modify strings in different ways.   

The *re.sub()* method returns the modified string as an output.


Learn more about  [*[SVG image]*](https://docs.python.org/2/library/re.html#re.sub) .


**Transformation of Strings** 


**Code** 



```
import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")

```

**Output** 



```
1 4 9 16 25 36 49 64 81

```

  

**Replacements in Strings**


**Code** 



```
import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment

```

**Output**



```
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>

```



---


**Task**


You are given a text of  *[SVG image]*  lines. The text contains `&&` and `||` symbols.   

Your task is to modify those symbols to the following: 



```
&& → and
|| → or

```

Both `&&` and `||` should have a *space* " " on both sides. 

**Input Format**

The first line contains the integer,  *[SVG image]* .   

 The next  *[SVG image]*  lines each contain a line of the text.


**Constraints**


 *[SVG image]*  


Neither `&&` nor `||` occur in the *start* or *end* of each line. 

**Output Format**

Output the modified text.

**Sample Input**


```
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

```
**Sample Output**


```
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.    

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Regex Substitution](./regex_substitution.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/re-sub-regex-substitution/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/re-sub-regex-substitution/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/re-sub-regex-substitution/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/re-sub-regex-substitution/editorial) |

