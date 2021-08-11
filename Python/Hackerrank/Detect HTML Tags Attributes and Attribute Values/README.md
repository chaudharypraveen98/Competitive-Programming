## **[Detect HTML Tags, Attributes and Attribute Values](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values)** 
You are given an HTML code snippet of lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.<br>Print the detected items in the following format:
```
Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]
```

<br><br>The <code>-&gt;</code> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value. <br>
The <code>&gt;</code> symbol acts as a separator of attributes and attribute values.<br><br><strong>Note:</strong> Do not detect any <em>HTML</em> tag, attribute or attribute value inside the <em>HTML</em> comment tags (<code>&lt;!-- Comments --&gt;</code>). Comments can be multiline.<br>
All attributes have an attribute value.

#### Sample Input
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

#### Sample Output
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

#### Explanation

head tag: Print the head tag only because it has no attribute.

title tag: Print the title tag only because it has no attribute.

object tag: Print the object tag. In the next  lines, print the attributes type, data, width and                     height along with their respective values.

<p><!-- Comment --> tag: Don't detect anything inside it.</p>

param tag: Print the param tag. In the next  lines, print the attributes name along with                     their respective values.