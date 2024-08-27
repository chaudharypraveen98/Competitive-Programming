## [Tag Content Extractor](https://www.hackerrank.com/challenges/tag-content-extractor)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Medium       | 20      | 95.51%        |

In a tag\-based language like *XML* or *HTML*, contents are enclosed between a *start tag* and an *end tag* like `<tag>contents</tag>`. Note that the corresponding *end tag* starts with a `/`.


Given a string of text in a tag\-based language, parse this text and retrieve the contents enclosed within sequences of well\-organized tags meeting the following criterion:


1. The name of the *start* and *end* tags must be same. The HTML code `<h1>Hello World</h2>` is *not valid*, because the text starts with an `h1` tag and ends with a non\-matching `h2` tag.
2. Tags can be nested, but content between nested tags is considered *not valid*. For example, in `<h1><a>contents</a>invalid</h1>`, `contents` is *valid* but `invalid` is *not valid*.
3. Tags can consist of any printable characters.
**Input Format**

The first line of input contains a single integer,  *[SVG image]*  (the number of lines).   

The  *[SVG image]*  subsequent lines each contain a line of text.


**Constraints** 


* *[SVG image]*
* Each line contains a maximum of  *[SVG image]*  printable characters.
* The total number of characters in all test cases will not exceed  *[SVG image]* .
**Output Format**

For each line, print the content enclosed within valid tags.   

If a line contains multiple instances of valid content, print out each instance of valid content on a new line; if no valid content is found, print `None`.

**Sample Input**


```
4
<h1>Nayeem loves counseling</h1>
<h1><h1>Sanjay has no watch</h1></h1><par>So wait for a while</par>
<Amee>safat codes like a ninja</amee>
<SA premium>Imtiaz has a secret crush</SA premium>

```
**Sample Output**


```
Nayeem loves counseling
Sanjay has no watch
So wait for a while
None
Imtiaz has a secret crush

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Tag Content Extractor](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/tag-content-extractor/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/tag-content-extractor/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/tag-content-extractor/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/tag-content-extractor/editorial) |

