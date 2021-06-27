## **[XML 1 - Find the Score](https://www.hackerrank.com/challenges/xml-1-find-the-score)** 
You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.

#### Input Format
The first line contains *N*, the number of lines in the XML document.
The next lines *N* follow containing the XML document.

#### Output Format
Output a single line, the integer score of the given XML document.

#### Sample Input
```
6
<feed xml:lang='en'>
    <title>HackerRank</title>
     Programming challenges
       />
    2013-12-25T12:00:00</updated>
</feed>
```

#### Sample Output
`5`

#### Explanation
The feed and subtitle tag have one attribute each - lang.
The title and updated tags have no attributes.
The link tag has three attributes - rel, type and href.

So, the total score is *1 + 1 + 3 = 5*.

There may be any level of nesting in the XML document. To learn about XML parsing, refer here.

**NOTE**: In order to parse and generate an XML element tree, use the following code:
```
>> import xml.etree.ElementTree as etree
>> tree = etree.ElementTree(etree.fromstring(xml))
```
Here, XML is the variable containing the string.
Also, to find the number of keys in a dictionary, use the len function:
```
>> dicti = {'0': 'This is zero', '1': 'This is one'}
>> print (len(dicti))

2
```