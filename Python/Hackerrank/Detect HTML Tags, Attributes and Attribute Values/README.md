## [Detect HTML Tags, Attributes and Attribute Values](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    30     |        97.61% |

You are given an HTML code snippet of lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.


Print the detected items in the following format:



```
Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]

```

  



The `->` symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.   

The `>` symbol acts as a separator of attributes and attribute values.


If an HTML tag has no attribute then simply print the name of the tag.


**Note:** Do not detect any *HTML* tag, attribute or attribute value inside the *HTML* comment tags (`<!-- Comments -->`). Comments can be multiline.  

All attributes have an attribute value.

**Input Format**

The first line contains an integer  *[SVG image]* , the number of lines in the *HTML* code snippet.  

The next  *[SVG image]*  lines contain *HTML* code.


**Constraints**


 *[SVG image]* 

**Output Format**

Print the *HTML* tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.  



Format your answers as explained in the problem statement.

**Sample Input**


```
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

```
**Sample Output**


```
head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high

```
**Explanation**

* **head** tag: Print the *head* tag only because it has no attribute.
* **title** tag: Print the *title* tag only because it has no attribute.
* **object** tag: Print the *object* tag. In the next  *4*  lines, print the attributes *type*, *data*, *width* and *height* along with their respective values.
* **\<!\-\- Comment \-\-\>** tag: Don't detect anything inside it.
* **param** tag: Print the *param* tag. In the next  *2*  lines, print the attributes *name* along with their respective *values*.

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Detect HTML Tags, Attributes and Attribute Values](./detect_html_tags_attributes_and_attribute_values.py)

| Submissions                                                                                                           |                                                        Leaderboard                                                         |                                                                                                           Discussions |                                                                                                       Editorial |
| :-------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/editorial) |

